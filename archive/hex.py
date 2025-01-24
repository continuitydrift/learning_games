class InteractiveHexagonalGrid(HexagonalGrid):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        """Detect which hexagon was clicked and change its color."""
        # Determine clicked hexagon based on event.x and event.y
        # (Implementation depends on hex grid logic)
        self.setCell(1, 1, fill="pink")  # Example action
