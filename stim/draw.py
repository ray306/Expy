from expy import shared
from expy.colors import *
from expy.io import sendTrigger

np = shared.np
math = shared.math

def getPos(x=shared.win_width // 2, y=shared.win_height // 2, w=0, h=0, anchor_x='center', anchor_y='center'):
    '''
    Caluate the screen position of object

    Parameters
    ----------
    x: float or int (default: shared.win_width // 2)
        If x is float, it represents the x-offset(-1~1 scale) from the object benchmark to the screen center,
        if int, it represents the x-offset(pixel) from the object benchmark to the screen upperleft.
    y: float or int (default: shared.win_height // 2)
        Similar with x
    w: float or int (default: 0)
        If w is float, it represents the width scale on screen,
        if int, it represents the width in pixel.
    h: float or int (default: 0)
        Similar with x 
    anchor_x: str (default:'center')
        The position benchmark on this object to the given x.
        Options: 'center', 'left', or 'right'.
    anchor_y: str (default:'center')
        The position benchmark on this object to the given y.
        Options: 'center', 'top', or 'bottom'.


    Returns
    -------
    (x, y): (int, int)
        The position of the object's lowerleft corner

    '''
    if type(x) is float:
        x, y = (0.5 + x / 2) * \
            shared.win_width, (0.5 + y / 2) * shared.win_height
    if w < 1:
        w, h = w * shared.win_width, h * shared.win_height

    if anchor_x == 'center':
        x = x - w / 2
    elif anchor_x == 'right':
        x = x - w
    elif anchor_x == 'left':
        x = x
    else:
        raise ValueError('Unsupported position benchmark')

    if anchor_y == 'center':
        y = y - h / 2
    elif anchor_y == 'top':
        y = y - h
    elif anchor_y == 'bottom':
        y = y
    else:
        raise ValueError('Unsupported position benchmark')

    if w>0:
        return int(x), int(y), int(w), int(h)
    else:
        return int(x), int(y)


def drawText(text, font=shared.default_font, size='stim_font_size', color=C_white, rotation=0, x=0.0, y=0.0, anchor_x='center', anchor_y='center', show_now=True, display=True, timeit=False, trigger=None):
    '''
    Draw text with complex format on the canvas. The text will show as multiple lines splited by the '\n'. 

    Parameters
    ----------
    text: str
        The content of text.
    font: str (default: shared.default_font)
        The font name of text.
    size:int, or str (default: 'stim_font_size')
        The font size of text, you can either use a number or a pre-defined number name.
    color: RGB tuple, or pre-defined variable (default:'C_white')
        The font color of text, you can either use an RGB value or a pre-defined color name. 
        The pre-defined colors include C_black, C_white, C_red, C_lime, C_blue, C_yellow, C_aqua, C_fuchsia, C_silver, C_gray, C_maroon, C_olive, C_green, C_purple, C_teal, C_navy.
    rotation: int (default: 0)
        The rotation angle of text.
    x: int, or float (default: 0.0)
        The x coordinate of text. If x is int, the coordinate would be pixel number to the left margin of screen; If x is float (-1~1), the coordinate would be percentage of half screen to the screen center.
    y: int, or float (default: 0.0)
        The y coordinate of text. If y is int, the coordinate would be pixel number to the upper margin of screen; If y is float (-1~1), the coordinate would be percentage of half screen to the screen center.
    anchor_x: str (default: 'center')
        The position benchmark on this object to the given x.
        Options: 'center', 'left', or 'right'.
    anchor_y: str (default: 'center')
        The position benchmark on this object to the given y.
        Options: 'center', 'top', or 'bottom'.
    show_now: True(default), False
        If True, the function will put the canvas onto the screen immediately (with a potential delay);
        otherwise, the canvas will be put until `show` function.
    (beta testing) trigger: (content, mode)
    (beta testing) timeit: True, False (default)
    
    Returns
    -------
    None
    '''
    if display==False:
        show_now = False
        print('WARNING: The "display" will be deprecated in future version. Please use "show_now" instead')

    'Assign value'
    if (type(size) is str) and (size in shared.font):
        size = shared.font[size]
    elif (type(size) is int) and (size > 0):
        pass
    else:
        raise ValueError(str(size) + ' cannot be regarded as a font size')

    x, y = getPos(x, y)

    'Draw'
    if not '\n' in text:
        label = shared.pyglet.text.Label(text,
                                         color=color,
                                         font_name=font, font_size=size,
                                         x=x, y=y,
                                         anchor_x=anchor_x, anchor_y=anchor_y)
        label.draw()

    else:
        lines = text.split('\n')
        row_spacing = 0.5  # 0.5x row spacing
        y_offset_all = - ((1 + row_spacing) * len(lines) -
                          row_spacing) * size / 2
        for ind, target in enumerate(lines):
            y_offset = y_offset_all + (1 + row_spacing) * ind * size
            label = shared.pyglet.text.Label(target,
                                             color=color,
                                             font_name=font, font_size=size,
                                             x=x, y=y - y_offset,
                                             anchor_x=anchor_x, anchor_y=anchor_y)
            label.draw()

    if show_now:
        shared.win.flip()
        if timeit and not shared.start_tp:
            now = shared.time.time()
            shared.start_tp = now
        if trigger:
            sendTrigger(trigger[0], mode=trigger[1])
    else:
        shared.need_update = True


def drawRect(w, h, x=0.0, y=0.0, fill=True, color=C_white, width=1, anchor_x='center', anchor_y='center', show_now=True, display=True, timeit=False, trigger=None):
    '''
    Draw rectangle on the canvas.

    Parameters
    ----------
    w: float or int (default: 0)
        The width of rectangle.
        If w is float, it represents the width scale on screen,
        if int, it represents the width in pixel.
    h: float or int (default: 0)
        The height of rectangle.
        Similar with x. 
    x: int, or float (default:0.0)
        The x coordinate of rectangle.
        If x is int, the coordinate would be pixel number to the left margin of screen;
        If x is float (-1~1), the coordinate would be percentage of half screen to the screen center.
    y: int, or float (default:0.0)
        The y coordinate of rectangle.
        If y is int, the coordinate would be pixel number to the upper margin of screen;
        If y is float (-1~1), the coordinate would be percentage of half screen to the screen center.
    fill: True(default), False
        Whether to fill out the blank in rectangle
    color: RGB tuple, or pre-defined variable (default:'C_white')
        The font color of text, you can either use an RGB value or a pre-defined color name. 
        The pre-defined colors include C_black, C_white, C_red, C_lime, C_blue, C_yellow, C_aqua, C_fuchsia, C_silver, C_gray, C_maroon, C_olive, C_green, C_purple, C_teal, C_navy.
    width: int (default: 1)
        The width of each line
    anchor_x: str (default:'center')
        The position benchmark on this object to the given x.
        Options: 'center', 'left', or 'right'.
    anchor_y: str (default:'center')
        The position benchmark on this object to the given y.
        Options: 'center', 'top', or 'bottom'.
    show_now: True(default), False
        If True, the function will put the canvas onto the screen. 
    (beta testing) trigger: (content, mode)
    (beta testing) timeit: True, False (default)
    
    Returns
    -------
    None
    '''
    if display==False:
        show_now = False
        print('WARNING: The "display" will be deprecated in future version. Please use "show_now" instead')

    x, y, w, h = getPos(x, y, w=w, h=h, anchor_x='center', anchor_y='center')

    points = [x, y, x + w, y, x + w, y + h, x, y + h]

    if fill:
        shared.pyglet.graphics.draw_indexed(4, shared.gl.GL_TRIANGLES,
                                            [0, 1, 2, 0, 2, 3],
                                            ('v2i', points),
                                            ('c4B', color * 4)
                                            )
    else:
        shared.pyglet.gl.glLineWidth(width)
        shared.pyglet.graphics.draw(4, shared.gl.GL_LINE_LOOP,
                                    ('v2i', points),
                                    ('c4B', color * 4)
                                    )

    if show_now:
        shared.win.flip()
        if timeit and not shared.start_tp:
            now = shared.time.time()
            shared.start_tp = now
        if trigger:
            sendTrigger(trigger[0], mode=trigger[1])
    else:
        shared.need_update = True


def drawCircle(r, x=0.0, y=0.0, fill=True, color=C_white, width=1, anchor_x='center', anchor_y='center', show_now=True, display=True, timeit=False, trigger=None):
    '''
    Draw circle on the canvas.

    Parameters
    ----------
    r: int
        The radius of circle in pixel.
    x: int, or float (default:0.0)
        The x coordinate of circle.
        If x is int, the coordinate would be pixel number to the left margin of screen;
        If x is float (-1~1), the coordinate would be percentage of half screen to the screen center.
    y: int, or float (default:0.0)
        The y coordinate of circle.
        If y is int, the coordinate would be pixel number to the upper margin of screen;
        If y is float (-1~1), the coordinate would be percentage of half screen to the screen center.
    fill: True(default), False
        Whether to fill out the blank in circle
    color: RGB tuple, or pre-defined variable (default:'C_white')
        The font color of text, you can either use an RGB value or a pre-defined color name. 
        The pre-defined colors include C_black, C_white, C_red, C_lime, C_blue, C_yellow, C_aqua, C_fuchsia, C_silver, C_gray, C_maroon, C_olive, C_green, C_purple, C_teal, C_navy.
    width: int (default: 1)
        The width of each line
    anchor_x: str (default:'center')
        The position benchmark on this object to the given x.
        Options: 'center', 'left', or 'right'.
    anchor_y: str (default:'center')
        The position benchmark on this object to the given y.
        Options: 'center', 'top', or 'bottom'.
    show_now: True(default), False
        If True, the function will put the canvas onto the screen. 
    (beta testing) trigger: (content, mode)
    (beta testing) timeit: True, False (default)
    
    Returns
    -------
    None
    '''
    if display==False:
        show_now = False
        print('WARNING: The "display" will be deprecated in future version. Please use "show_now" instead')

    x, y = getPos(x, y, anchor_x='center', anchor_y='center')

    if fill:
        numPoints = int(2 * r * math.pi)
        s = math.sin(2 * math.pi / numPoints)
        c = math.cos(2 * math.pi / numPoints)

        dx, dy = r, 0

        shared.gl.glBegin(shared.gl.GL_TRIANGLE_FAN)
        shared.gl.glColor4f(*color)
        shared.gl.glVertex2f(x, y)
        for i in range(numPoints + 1):
            shared.gl.glVertex2f(x + dx, y + dy)
            dx, dy = (dx * c - dy * s), (dy * c + dx * s)
        shared.gl.glEnd()
    else:
        numPoints = int(2 * r * math.pi)
        verts = []
        for i in range(numPoints):
            angle = math.radians(float(i) / numPoints * 360.0)
            verts += [r * math.cos(angle) + x, r * math.sin(angle) + y]

        circle = shared.pyglet.graphics.vertex_list(numPoints,
                                                    ('v2f', verts),
                                                    ('c4B', color * numPoints))
        shared.gl.glClear(shared.pyglet.gl.GL_COLOR_BUFFER_BIT)
        # shared.gl.glColor4b(*color)
        circle.draw(shared.gl.GL_LINE_LOOP)

    if show_now:
        if trigger:
            sendTrigger(trigger[0], mode=trigger[1])
        if trigger:
            sendTrigger(trigger[0], mode=trigger[1])
        shared.win.flip()
    else:
        shared.need_update = True


def drawPoints(points, color=C_white, size=1, show_now=True, display=True, timeit=False, trigger=None):
    '''
    Draw point(s) on the canvas.

    Parameters
    ----------
    points: list of tuple
        The x-y points list
        If the x,y are given as float, they would be interpret as an relative position[-1~+1] to the center on the screen;
        or if they are given as int, they would be interpret as pixel indicators to the lowerleft corner on the screen.
        Examples:
            [(0.0,0.0), (0.5,0), (0.5,0.5)]
    color: RGB tuple, or pre-defined variable (default:'C_white')
        The font color of text, you can either use an RGB value or a pre-defined color name. 
        The pre-defined colors include C_black, C_white, C_red, C_lime, C_blue, C_yellow, C_aqua, C_fuchsia, C_silver, C_gray, C_maroon, C_olive, C_green, C_purple, C_teal, C_navy.
    size: int (default: 1)
        The size of each point
    show_now: True(default), False
        If True, the function will put the canvas onto the screen. 
    (beta testing) trigger: (content, mode)
    (beta testing) timeit: True, False (default)
    
    Returns
    -------
    None
    '''
    if display==False:
        show_now = False
        print('WARNING: The "display" will be deprecated in future version. Please use "show_now" instead')

    new_points = []
    for x, y in points:
        if type(x) is float:
            new_points += [(0.5 + x / 2) * shared.win_width,
                           (0.5 + y / 2) * shared.win_height]
        else:
            new_points += [x, y]

    shared.gl.glPointSize(size)
    shared.pyglet.graphics.draw(len(new_points) // 2, shared.gl.GL_POINTS,
                                ('v2i', new_points),
                                ('c4B', color * (len(new_points) // 2))
                                )

    if show_now:
        shared.win.flip()
        if timeit and not shared.start_tp:
            now = shared.time.time()
            shared.start_tp = now
        if trigger:
            sendTrigger(trigger[0], mode=trigger[1])
    else:
        shared.need_update = True


def drawLines(points, color=C_white, width=1, close=False, show_now=True, display=True, timeit=False, trigger=None):
    '''
    Draw line(s) on the canvas.

    Parameters
    ----------
    points: list of tuple
        The turning x-y points of lines
        If the x,y are given as float, they would be interpret as an relative position[-1~+1] to the center on the screen;
        or if they are given as int, they would be interpret as pixel indicators to the lowerleft corner on the screen.
        Examples:
            [(0.0,0.0), (0.5,0), (0.5,0.5)]
    color: RGB tuple, or pre-defined variable (default:'C_white')
        The font color of text, you can either use an RGB value or a pre-defined color name. 
        The pre-defined colors include C_black, C_white, C_red, C_lime, C_blue, C_yellow, C_aqua, C_fuchsia, C_silver, C_gray, C_maroon, C_olive, C_green, C_purple, C_teal, C_navy.
    width: int (default: 1)
        The width of each line
    close: True, False(default)
        Whether to connect the last point with the first one. 
        If True, the polygon could be drawn.
    show_now: True(default), False
        If True, the function will put the canvas onto the screen.
    (beta testing) trigger: (content, mode)
    (beta testing) timeit: True, False (default)
    
    Returns
    -------
    None
    '''
    if display==False:
        show_now = False
        print('WARNING: The "display" will be deprecated in future version. Please use "show_now" instead')

    new_points = []
    if close:
        points += points[0]
    for x, y in points:
        if type(x) is float:
            new_points += [(0.5 + x / 2) * shared.win_width,
                           (0.5 + y / 2) * shared.win_height]
        else:
            new_points += [x, y]

    shared.pyglet.gl.glLineWidth(width)
    shared.pyglet.graphics.draw(len(new_points) // 2, shared.gl.GL_LINE_STRIP,
                                ('v2i', new_points),
                                ('c4B', color * (len(new_points) // 2))
                                )

    if show_now:
        shared.win.flip()
        if timeit and not shared.start_tp:
            now = shared.time.time()
            shared.start_tp = now
        if trigger:
            sendTrigger(trigger[0], mode=trigger[1])
    else:
        shared.need_update = True


def drawPic(path, w=0, h=0, x=0.0, y=0.0, rotate=0, anchor_x='center', anchor_y='center', show_now=True, display=True, timeit=False, trigger=None):
    '''
    Draw loaded image on the canvas.

    Parameters
    ----------
    path: str
        The file path of target image
    w: int(default:0), or float 
        The width of image.
        If w is float, it represents the width scale on screen;
        if int, it represents the width in pixel.
    h: int(default:0), or float 
        The height of image.
        If w is float, it represents the height scale on screen;
        if int, it represents the height in pixel.
    x: int, or float (default:0.0)
        The x coordinate of image.
        If x is int, the coordinate would be pixel number to the left margin of screen;
        If x is float (-1~1), the coordinate would be percentage of half screen to the screen center.
    y: int, or float (default:0.0)
        The y coordinate of image.
        If y is int, the coordinate would be pixel number to the upper margin of screen;
        If y is float (-1~1), the coordinate would be percentage of half screen to the screen center.
    rotation: int (default:0)
        The rotation angle of object.
    anchor_x: str (default:'center')
        The position benchmark on this object to the given x.
        Options: 'center', 'left', or 'right'.
    anchor_y: str (default:'center')
        The position benchmark on this object to the given y.
        Options: 'center', 'top', or 'bottom'.
    show_now: True(default), False
        If True, the function will put the canvas onto the screen. 
    (beta testing) trigger: (content, mode)
    (beta testing) timeit: True, False (default)
    
    Returns
    -------
    None
    '''
    if display==False:
        show_now = False
        print('WARNING: The "display" will be deprecated in future version. Please use "show_now" instead')

    im = shared.pyglet.image.load(path)

    if type(w) is float:
        w = (0.5 + w / 2) * shared.win_width
    if type(h) is float:
        h = (0.5 + h / 2) * shared.win_height

    if w > 0 and h > 0:
        im = im.get_texture()
        shared.gl.glTexParameteri(
            shared.gl.GL_TEXTURE_2D,
            shared.gl.GL_TEXTURE_MAG_FILTER,
            shared.gl.GL_NEAREST)
        im.width = w
        im.height = h
    else:
        w, h = im.width, im.height

    x, y, w, h = getPos(x, y, w, h, anchor_x=anchor_x, anchor_y=anchor_y)

    im.blit(x, y, 0)

    if show_now:
        shared.win.flip()
        if timeit and not shared.start_tp:
            now = shared.time.time()
            shared.start_tp = now
        if trigger:
            sendTrigger(trigger[0], mode=trigger[1])
    else:
        shared.need_update = True
