; Compilar - Transforma o programa para linguagem máquina
;   nasm -f elf64 hello.asm
; Linkeditar - Transformar o programa em linguagem de máquina para um executável
;   ld -s -o hello hello.o

section .data
    msg db 'Hello, World!', 0xA
    tam equ $- msg ; Número de caracteres da msg

section .text

global _start

_start: ; inicio do programa
    mov eax, 0x4 
    mov ebx, 0x1
    mov ecx, msg
    mov edx, tam
    int 0x80

saida: ; Opcional, Não atrapalha o fluxo do programa, serve para organizar-lo
    mov eax, 0x1 ; SO, estou terminando o programa
    mov ebx, 0x0 ; SO, o valor de retorno é 0
    int 0x80 ; Executa todas as movimentações
