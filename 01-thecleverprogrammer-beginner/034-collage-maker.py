from PIL import Image


def vertical_collage(img1, img2, output_file):
    images = [Image.open(x) for x in [img1, img2]]
    widths, heights = zip(*(i.size for i in images))

    total_heights = sum(heights)
    max_widths = max(widths)

    new_im = Image.new('RGB', (max_widths, total_heights))

    y_offset = 0
    for im in images:
        new_im.paste(im, (0, y_offset))
        y_offset += im.size[1]

    new_im.save(output_file)


def horizontal_collage(img1, img2, output_file):
    images = [Image.open(x) for x in [img1, img2]]
    widths, heights = zip(*(i.size for i in images))

    total_widths = sum(widths)
    max_heights = max(heights)

    new_im = Image.new('RGB', (total_widths, max_heights))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save(output_file)


vertical_collage('resources/4.jpg', 'resources/5.jpg', 'resources/6.jpg')
horizontal_collage('resources/1.jpg', 'resources/2.jpg', 'resources/3.jpg')
