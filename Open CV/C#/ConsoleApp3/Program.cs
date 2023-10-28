using Emgu.CV;
using Emgu.CV.CvEnum;
using Emgu.CV.Structure;
using System;
using System.Windows.Forms;

class Program
{
    [STAThread]
    static void Main()
    {
        // Inicializa la cámara web (puedes cambiar el índice si tienes varias cámaras)
        VideoCapture capture = new VideoCapture(0);

        // Crea una ventana para mostrar el video
        CvInvoke.NamedWindow("Cámara Web", WindowMode.Normal);

        // Define un bucle para capturar y mostrar los fotogramas en tiempo real
        while (true)
        {
            // Captura un fotograma de la cámara web
            Mat frame = new Mat();
            capture.Read(frame);

            // Muestra el fotograma en la ventana
            CvInvoke.Imshow("Cámara Web", frame);

            // Espera un tiempo (en milisegundos) y verifica si se presiona la tecla 'Esc' (código 27) para salir
            if (CvInvoke.WaitKey(1) == 27)
                break;
        }

        // Libera los recursos
        capture.Dispose();
        CvInvoke.DestroyAllWindows();
    }
}
