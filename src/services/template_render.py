from PIL import Image


class TemplateRenderer:
    def __init__(self, template_path: str):
        self.template = template_path

    def place_qr(self, qr_img: Image.Image, positions: list[tuple[int, int]]) -> Image.Image:
        template = Image.open(self.template).convert("RGBA")
        qr_img = qr_img.convert("RGBA")

        for pos in positions:
            template.paste(qr_img, pos, qr_img)
        return template
