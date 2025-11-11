# Creado por Pedro :P  
# Comentado por ChatGPT  
import math
import wave
import struct
import itertools
from PIL import Image
import tkinter as tk
from tkinter import ttk, filedialog

# --- Osciladores básicos ---
def sine_osc(freq, amp=1.0, sample_rate=44100):
    """Generador de onda senoide."""
    increment = 2.0 * math.pi * freq / sample_rate
    phase = 0.0
    while True:
        yield amp * math.sin(phase)
        phase += increment
        if phase > 2.0 * math.pi:
            phase -= 2.0 * math.pi

def square_osc(freq, amp=1.0, sample_rate=44100):
    """Generador de onda cuadrada."""
    period = sample_rate / freq
    count = 0
    while True:
        yield amp * (1.0 if (count < period/2) else -1.0)
        count += 1
        if count >= period:
            count = 0

def saw_osc(freq, amp=1.0, sample_rate=44100):
    """Generador de onda diente de sierra."""
    increment = 2.0 * amp / (sample_rate / freq)
    val = -amp
    while True:
        yield val
        val += increment
        if val >= amp:
            val = -amp

# --- Funciones de imagen y sonido ---
def extraer_pixeles(ruta_imagen, modo_grises=False):
    """Extrae matriz de valores de píxel de imagen."""
    img = Image.open(ruta_imagen)
    if modo_grises:
        img = img.convert('L')
    ancho, alto = img.size
    matriz = []
    for y in range(alto):
        fila = []
        for x in range(ancho):
            valor = img.getpixel((x, y))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def pixel_a_parametros(valor_pix, valor_pix2, valor_pix3,
                        minf, maxf, amp_scale, dur_por_pixel,
                        mapa_canales):
    """
    Mapea valores de píxel a parámetros de sonido:
    - freq: frecuencia
    - amp: amplitud
    - dur: duración
    Dependiendo de `mapa_canales` se usa distinto canal para distinto parámetro.
    """
    # por defecto: R→freq, G→amp, B→dur
    if mapa_canales == 'R→freq, G→amp, B→dur':
        freq = minf + (valor_pix / 255.0) * (maxf - minf)
        amp = amp_scale * (valor_pix2 / 255.0)
        dur = dur_por_pixel * (valor_pix3 / 255.0 + 0.1)
    elif mapa_canales == 'R→amp, G→freq, B→dur':
        freq = minf + (valor_pix2 / 255.0) * (maxf - minf)
        amp = amp_scale * (valor_pix / 255.0)
        dur = dur_por_pixel * (valor_pix3 / 255.0 + 0.1)
    else:
        # fallback al mapeo sencillo
        freq = minf + (valor_pix / 255.0) * (maxf - minf)
        amp = amp_scale
        dur = dur_por_pixel

    return freq, amp, dur

def generar_frames(matriz, tipo_osc, sample_rate,
                    minf, maxf, amp_scale, dur_por_pixel, mapa_canales, modo_grises):
    """Genera la lista de muestras de audio a partir de la matriz de píxeles."""
    frames = []
    for fila in matriz:
        for valor in fila:
            if modo_grises:
                # valor es único --> aplicar igual a R, G, B
                r = valor
                g = valor
                b = valor
            else:
                r, g, b = valor
            freq, amp, dur = pixel_a_parametros(r, g, b,
                                                 minf, maxf, amp_scale,
                                                 dur_por_pixel, mapa_canales)
            if tipo_osc == 'seno':
                osc = sine_osc(freq, amp, sample_rate)
            elif tipo_osc == 'cuadrado':
                osc = square_osc(freq, amp, sample_rate)
            elif tipo_osc == 'diente de sierra':
                osc = saw_osc(freq, amp, sample_rate)
            else:
                osc = sine_osc(freq, amp, sample_rate)
            num_muestras = int(dur * sample_rate)
            for _ in range(num_muestras):
                frames.append(next(osc))
    return frames

def guardar_wav(frames, ruta_salida, sample_rate=44100):
    """Guarda los frames como archivo WAV mono de 16 bits."""
    with wave.open(ruta_salida, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        for f in frames:
            if f > 1.0: f = 1.0
            if f < -1.0: f = -1.0
            val = int(f * 32767.0)
            data = struct.pack('<h', val)
            wf.writeframesraw(data)
        wf.writeframes(b'')

# --- Interfaz gráfica ---
class App:
    def __init__(self, root):
        self.root = root
        root.title("Generador de Sonido desde Imagen")
        
        # Variables modificables por usuario
        self.ruta_imagen = tk.StringVar(value="gato.png")
        self.modo_grises = tk.BooleanVar(value=False)
        self.minf = tk.DoubleVar(value=200.0)
        self.maxf = tk.DoubleVar(value=2000.0)
        self.dur_por_pixel = tk.DoubleVar(value=0.005)
        self.amp_scale = tk.DoubleVar(value=0.5)
        self.tipo_osc = tk.StringVar(value='seno')
        self.mapa_canales = tk.StringVar(value='R→freq, G→amp, B→dur')
        
        # Widgets de la GUI
        ttk.Label(root, text="Ruta de la imagen:").grid(column=0, row=0, sticky='w')
        ttk.Entry(root, textvariable=self.ruta_imagen, width=30).grid(column=1, row=0)
        ttk.Button(root, text="Seleccionar...", command=self.seleccionar_imagen).grid(column=2, row=0)
        
        ttk.Checkbutton(root, text="Usar escala de grises", variable=self.modo_grises).grid(column=0, row=1, columnspan=2, sticky='w')
        
        ttk.Label(root, text="Frecuencia mínima (Hz):").grid(column=0, row=2, sticky='w')
        ttk.Entry(root, textvariable=self.minf).grid(column=1, row=2)
        
        ttk.Label(root, text="Frecuencia máxima (Hz):").grid(column=0, row=3, sticky='w')
        ttk.Entry(root, textvariable=self.maxf).grid(column=1, row=3)
        
        ttk.Label(root, text="Duración por píxel (s):").grid(column=0, row=4, sticky='w')
        ttk.Entry(root, textvariable=self.dur_por_pixel).grid(column=1, row=4)
        
        ttk.Label(root, text="Escala de amplitud:").grid(column=0, row=5, sticky='w')
        ttk.Entry(root, textvariable=self.amp_scale).grid(column=1, row=5)
        
        ttk.Label(root, text="Tipo de oscilador:").grid(column=0, row=6, sticky='w')
        ttk.OptionMenu(root, self.tipo_osc, self.tipo_osc.get(), 'seno','cuadrado','diente de sierra').grid(column=1, row=6, sticky='w')
        
        ttk.Label(root, text="Mapa de canales:").grid(column=0, row=7, sticky='w')
        ttk.OptionMenu(root, self.mapa_canales, self.mapa_canales.get(),
                       'R→freq, G→amp, B→dur',
                       'R→amp, G→freq, B→dur').grid(column=1, row=7, sticky='w')
        
        ttk.Button(root, text="Generar sonido", command=self.generar).grid(column=0, row=8, columnspan=3, pady=10)
        
    def seleccionar_imagen(self):
        """Permite al usuario seleccionar archivo de imagen."""
        ruta = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png *.jpg *.jpeg")])
        if ruta:
            self.ruta_imagen.set(ruta)
    
    def generar(self):
        """Recoge los parámetros, procesa la imagen y genera el archivo WAV."""
        ruta = self.ruta_imagen.get()
        modo_gr = self.modo_grises.get()
        minf = self.minf.get()
        maxf = self.maxf.get()
        dur_pix = self.dur_por_pixel.get()
        amp_scale = self.amp_scale.get()
        tipo_osc = self.tipo_osc.get()
        mapa = self.mapa_canales.get()
        
        print(f"Cargando imagen {ruta} … modo_grises={modo_gr}")
        matriz = extraer_pixeles(ruta, modo_grises=modo_gr)
        print("Generando frames de audio …")
        frames = generar_frames(matriz, tipo_osc, 44100,
                                 minf, maxf, amp_scale, dur_pix, mapa, modo_gr)
        print(f"Guardando archivo resultado.wav … (muestras: {len(frames)})")
        guardar_wav(frames, "resultado.wav", sample_rate=44100)
        print("¡Terminado! Archivo generado: resultado.wav")
        
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
