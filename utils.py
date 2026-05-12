def formata_valores(value, prefix=''):
    negativo = value < 0
    value = abs(value)

    for unit in ['', 'Mil', 'Mi']:
        if value < 1000:
            valor_formatado = f'{value:.2f} {unit}'.strip()
            break
        value /= 1000

    if negativo:
        valor_formatado = f'-{valor_formatado}'

    return f'{prefix} {valor_formatado}'.strip()