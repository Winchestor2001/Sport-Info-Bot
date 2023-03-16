from PIL import Image, ImageDraw, ImageFont


async def draw_table(data):
    image = f"{data['liga']}_table.jpg"
    output = f'draw_images/{image}'
    img = Image.open('images/' + image)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("fonts/MontserratAlternates-Bold.ttf", 30)
    draw.text((110, 50), "№", fill='#fff', font=font)
    draw.text((200, 50), "Jamoa", fill='#fff', font=font)
    w = 110
    h = 175
    for team in data['data']:
        # print(team)

        draw.text((w, h), str(team['place']), fill='#fff', font=font)
        w = 200
        draw.text((w, h), team['team'], fill='#fff', font=font)
        w = 725
        draw.text((w, h), str(team['games']), fill='#fff', font=font)
        w = 900
        draw.text((w, h), str(team['win']), fill='#fff', font=font)
        w = 1050
        draw.text((w, h), str(team['lose']), fill='#fff', font=font)
        w = 1190
        draw.text((w, h), str(team['goals']), fill='#fff', font=font)
        w = 1345
        draw.text((w, h), str(team['score']), fill='#fff', font=font)
        h += 70
        w = 110
    # img.show()
    img.save(output)
    return output
