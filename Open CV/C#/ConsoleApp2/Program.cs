using System;
using Emgu.CV;
using Emgu.CV.CvEnum;
using Emgu.CV.Structure;
using System.Drawing;
using Emgu.CV.Util;

class Program
{
    static void Main(string[] args)
    {
        // Umbral de porcentaje de píxeles azules para la detección
        double thresholdPercentage = 0.1;  // Cambia este valor según tus necesidades

        // Tamaño mínimo de área para la detección (ajusta este valor según tus necesidades)
        double minArea = 5000;

        // Inicializa la cámara web
        VideoCapture capture = new VideoCapture(0);

        // Define el rango de colores en formato HSV para el azul
        var lowerBlue = new Hsv(120, 50, 50);
        var upperBlue = new Hsv(160, 255, 255);

        // Configura el kernel para la dilatación
        Mat kernel = CvInvoke.GetStructuringElement(ElementShape.Rectangle, new Size(6, 6), new Point(-1, -1));

        while (true)
        {
            // Captura un cuadro de la cámara
            Mat frame = new Mat();
            capture.Read(frame);
            CvInvoke.Flip(frame, frame, FlipType.Horizontal); // Gira en modo espejo la imagen

            // Convierte la imagen a formato HSV
            Mat hsvFrame = new Mat();
            CvInvoke.CvtColor(frame, hsvFrame, ColorConversion.Bgr2Hsv);

            // Crea una máscara para el color azul
            Mat mask = new Mat();
            CvInvoke.InRange(hsvFrame, lowerBlue, upperBlue, mask);

            // Aplica una dilatación a la máscara
            CvInvoke.Dilate(mask, mask, kernel, new Point(-1, -1), 2, BorderType.Default, new MCvScalar(0));

            // Encuentra todos los contornos en la máscara
            VectorOfVectorOfPoint contours = new VectorOfVectorOfPoint();
            CvInvoke.FindContours(mask, contours, null, RetrType.External, ChainApproxMethod.ChainApproxSimple);

            // Inicializa listas para almacenar las coordenadas de los centros de los objetos detectados y sus áreas
            List<Point> centers = new List<Point>();
            List<double> areas = new List<double>();

            for (int i = 0; i < contours.Size; i++)
            {
                VectorOfPoint contour = contours[i];
                // Calcula el área del contorno
                double area = CvInvoke.ContourArea(contour);

                // Calcula el porcentaje de píxeles azules en el contorno
                Mat bluePixelsMask = new Mat();
                CvInvoke.BitwiseAnd(mask, mask, bluePixelsMask, contour);
                double bluePixels = CvInvoke.CountNonZero(bluePixelsMask);
                double bluePercentage = area > 0 ? bluePixels / area : 0;

                // Encuentra el centroide del contorno
                MCvMoments moments = CvInvoke.Moments(contour);
                if (moments.M00 != 0 && bluePercentage > thresholdPercentage && area > minArea)
                {
                    int centerX = (int)(moments.M10 / moments.M00);
                    int centerY = (int)(moments.M01 / moments.M00);
                    centers.Add(new Point(centerX, centerY));
                    areas.Add(area);
                }
            }

            // Ordena las áreas en orden descendente y almacena los índices de la lista ordenada
            int[] sortedIndexes = areas.Select((area, index) => new { Area = area, Index = index })
                .OrderByDescending(item => item.Area)
                .Select(item => item.Index)
                .ToArray();

            // Dibuja los contornos y asigna etiquetas a las áreas en función de su orden en la lista ordenada
            for (int i = 0; i < sortedIndexes.Length; i++)
            {
                int index = sortedIndexes[i];
                VectorOfPoint contour = contours[index];
                double area = areas[index];
                Point center = centers[index];

                // Dibuja el contorno del objeto en rojo
                CvInvoke.DrawContours(frame, contours, index, new MCvScalar(0, 0, 255), 2);
                // Dibuja el centroide del objeto en azul
                CvInvoke.Circle(frame, center, 5, new MCvScalar(255, 0, 0), -1);

                // Dibuja la etiqueta del área
                CvInvoke.PutText(frame, $"A {i + 1}", new Point(center.X + 10, center.Y),
                    FontFace.HersheyComplex, 0.6, new MCvScalar(0, 0, 255), 2);

                // Calcula el desplazamiento con respecto al centro de la pantalla para el objeto detectado
                int displacementX = center.X - frame.Cols / 2;
                int displacementY = center.Y - frame.Rows / 2;

                // Muestra el desplazamiento cerca del centroide del objeto
                string text = $"D = X: {displacementX}, Y: {displacementY}";
                CvInvoke.PutText(frame, text, new Point(center.X + 10, center.Y + 20),
                    FontFace.HersheyComplex, 0.6, new MCvScalar(0, 0, 0), 2);
            }

            // Dibuja el punto central en verde
            CvInvoke.Circle(frame, new Point(frame.Cols / 2, frame.Rows / 2), 5, new MCvScalar(0, 255, 0), -1);

            // Dibuja puntos en el plano cartesiano cada 20 unidades en x e y
            for (int i = 20; i < frame.Cols; i += 20)
            {
                CvInvoke.Circle(frame, new Point(i, frame.Rows / 2), 2, new MCvScalar(0, 255, 0), -1);
            }

            for (int j = 20; j < frame.Rows; j += 20)
            {
                CvInvoke.Circle(frame, new Point(frame.Cols / 2, j), 2, new MCvScalar(0, 255, 0), -1);
            }

            // Muestra el cuadro de la cámara en tiempo real
            CvInvoke.Imshow("Object Detection", frame);

            if (CvInvoke.WaitKey(1) == 'q')
                break;
        }

        // Libera los recursos
        capture.Dispose();
        CvInvoke.DestroyAllWindows();
    }
}
