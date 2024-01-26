def area_sum(rectangles):
    total_area = 0
    for rectangle in rectangles:
        height = rectangle["height"]
        width = rectangle["width"]
        area = height * width
        total_area += area
    return total_area
        
