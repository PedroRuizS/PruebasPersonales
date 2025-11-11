import cv2
from pyzbar.pyzbar import decode

# Inicializa la cámara
cap = cv2.VideoCapture(0)  # El '0' se refiere a la primera cámara conectada

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

print("Escáner de código de barras en tiempo real. Presiona 'q' para salir.")

while True:
    # Captura un frame de la cámara
    ret, frame = cap.read()
    if not ret:
        break

    # Convierte el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta y decodifica los códigos de barras
    barcodes = decode(gray)

    # Itera sobre los códigos de barras encontrados
    for barcode in barcodes:
        # Extrae los datos del código
        barcode_data = barcode.data.decode('utf-8')
        print(f"Código de barras detectado: {barcode_data}")

        # Opcionalmente, dibuja un rectángulo alrededor del código
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Muestra el número en el frame
        cv2.putText(frame, barcode_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Muestra el frame en una ventana
    cv2.imshow("Escáner de Código de Barras", frame)

    # Sale del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra todas las ventanas
cap.release()
cv2.destroyAllWindows()