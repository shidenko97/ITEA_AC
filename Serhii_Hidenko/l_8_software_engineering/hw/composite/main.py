from Serhii_Hidenko.l_8_software_engineering.hw.composite.dot import Dot
from Serhii_Hidenko.l_8_software_engineering.hw.composite.circle import Circle
from Serhii_Hidenko.l_8_software_engineering.hw.composite.compound_graphic import (
    CompoundGraphic,
)
from Serhii_Hidenko.l_8_software_engineering.hw.composite.image_editor import (
    ImageEditor,
)


if __name__ == "__main__":
    """
    - Compound pattern -
    Using when we create a tree, and all elements of tree using same methods
    with a each element of the tree. We can create a tree with any length of
    elements and all elements (including tree) will be using same methods.
    """

    # Create dot
    dot = Dot(1, 1)
    dot.draw()
    # Move dot
    dot.move(-1, 1)
    dot.draw()

    # Create circle
    circle = Circle(2, 2, 3)
    circle.draw()
    # Move circle
    circle.move(9, 5)
    circle.draw()

    # Create compound graphic
    compound = CompoundGraphic()
    # Add elements
    compound.add_component(dot)
    compound.add_component(circle)
    # Draw each element
    compound.draw()
    # Move each element
    compound.move(2, 2)
    # Draw each element
    compound.draw()

    # Create compound graphic
    compound2 = CompoundGraphic()
    # Add elements
    compound2.add_component(compound)
    compound2.add_component(Circle(100, 100, 100))
    # Draw each element
    compound2.draw()
    # Move each element
    compound2.move(0, 0)
    # Draw each element
    compound2.draw()

    # Using full tree
    editor = ImageEditor()
    editor.load()
    editor.group_selected(circle)
