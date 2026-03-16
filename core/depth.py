import torch
import cv2

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

midas = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")

midas.to(device)
midas.eval()

transforms = torch.hub.load("intel-isl/MiDaS", "transforms")

transform = transforms.small_transform


def get_depth_map(frame):

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    input_batch = transform(img).to(device)

    with torch.no_grad():

        prediction = midas(input_batch)

        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=img.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()

    depth_map = prediction.cpu().numpy()

    return depth_map