'''
Write a function to find the rectangular intersection of two rectangles.

They are defined as dictionaries like this:
    my_rectangle = {
        #Coordinates of bottom-left corner
        'left_x' : 1,
        'bottom_y' : 1,

        'width' : 6,
        'height' : 3,
    }

Takeaways:
    1) Breakdown the problem into subproblems: solve one axis at a time.
'''

def __find_overlap_in_line(start_point1, start_point2, point1_len, point2_len):
    intersect_start_point = max(start_point1, start_point2)
    intersect_end = min(start_point1 + point1_len, start_point2 + point2_len)
    if intersect_start_point >= intersect_end:
        return (None, None)
    else:
        return (intersect_start_point, intersect_end - intersect_start_point)

def find_rectangular_overlap(rect1, rect2):
    intersect_left_x, intersect_width = __find_overlap_in_line(rect1['left_x'], rect2['left_x'], rect1['width'], rect2['width'])
    intersect_bottom_y, intersect_height = __find_overlap_in_line(rect1['bottom_y'], rect2['bottom_y'], rect1['height'], rect2['height'])
    if intersect_width is None or intersect_height is None:
        return {'left_x': None,'bottom_y': None,'width': None,'height':None,}
    else:
        return { 'left_x' : intersect_left_x, 'bottom_y' : intersect_bottom_y, 'width' : intersect_width, 'height' : intersect_height}

rect1 = {'left_x':0, 'bottom_y':0, 'width':100, 'height':100}
rect2 = {'left_x':4, 'bottom_y':4, 'width':5, 'height':5}
print(find_rectangular_overlap(rect1, rect2))
