section .data
    message db 'Hello, World!', 0

section .text
    global _start

_start:
    ; Escribir el mensaje en la consola
    mov eax, 4         ; Número de sistema para la llamada "write" en Linux
    mov ebx, 1         ; Descriptor de archivo para la salida estándar (stdout)
    mov ecx, message   ; Dirección del mensaje
    mov edx, 13      ; Longitud del mensaje
    int 0x80           ; Llamada al sistema

    ; Salir del programa
    mov eax, 1         ; Número de sistema para la llamada "exit" en Linux
    xor ebx, ebx       ; Código de salida 0
    int 0x80           ; Llamada al sistema