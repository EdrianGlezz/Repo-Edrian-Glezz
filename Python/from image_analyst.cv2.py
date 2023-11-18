from image_analyst.cv2.utils import convert_image, create_frame_generator
from image_analyst.cv2.models import YoloV3OpenCV
from image_analyst.trackers import IOUTracker
import cv2

def report_callback(filename: str, current_size: float, total_size: float):
    print("{} {:.2f}%".format(filename, current_size/total_size*100), end="\r", flush=True)

model = YoloV3OpenCV.coco(report_callback=report_callback)

tracking_function = IOUTracker(model)

with create_frame_generator(0) as frame_generator:
    for frame in frame_generator:
        converted_frame = convert_image(frame, model.supported_format, model.supported_dtype)
        instances = tracking_function(converted_frame)

        for instance in instances:
            xmin, ymin, xmax, ymax = instance.bounding_box.as_tuple()

            text = "{} {} {:.2f}".format(instance.id, instance.class_name, instance.score)
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
            cv2.putText(frame, text, (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()