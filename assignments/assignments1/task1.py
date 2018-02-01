def allocate(message,letter):
    output = []
    for indx , char in enumerate(message):
        if char == letter:
            output.append(indx)
    return output




