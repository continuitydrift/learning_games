def create_hex_grid(width, height):
    hex_upper = "__/  \\"
    hex_lower = "  \\__/"

    grid = []
    for row in range(height):
        if row % 2 == 0:
            grid.append(hex_upper * width)
        else:
            grid.append(hex_lower * width)

    return "\n".join(grid)

# Example usage:
print(create_hex_grid(6, 6))
