using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.IO;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BotonMantenido
{
    public partial class MES : Form
    {
        public MES()
        {
            InitializeComponent();

        }

        public string CallToWebService(string SerialNumber)
        {
            try
            {
                JabilMES.MES_TISSoapClient Check = new JabilMES.MES_TISSoapClient();
                var Test = Check.OKToTest("Dyson", "Dyson", SerialNumber, "2", "JBL308CSNAP_JBL308CL100103", "JBL308CSNAP");
                //var Test = Check.OKToTest("Dyson", "Dyson", SerialNumber, "1", "JBL3080BGPT_JBL3080L100101", "BGPT");
                string result = Test.ToString();

                if (result == "PASS") return result;
                else return "NoPASS";

            }

            catch
            {
                return "Error";
            }

        }

        public string SendToMES(string serialNumber, string PowerP1B1, string PowerP2B2, string FlowP1B1, string PassOrFail)
        {
            double PP1 = double.Parse(PowerP1B1);
            double PP2 = double.Parse(PowerP2B2);
            double FP1 = double.Parse(FlowP1B1);
            //double FP2 = double.Parse(FlowP2B2);
            //double HP1 = double.Parse(HeatP1B1);
            //double HP2 = double.Parse(HeatP2B2);

            //double PHV = 5.0;
            //double PHL = 0.0;
            //double FHV = 5.0;
            //double FHL = 0.0;
            //double HHV = 5.0;
            //double HHL = 0.0;

            //string PP1R = "";
            //string PP2R = "";
            //string FP1R = "";
            //string FP2R = "";
            //string HP1R = "";
            //string HP2R = "";

            //if (PP1 < PHV || PP1 > PHL) PP1R = "Pass";
            //else PP1R = "Fail";
            //if (PP2 < PHV || PP2 > PHL) PP2R = "Pass";
            //else PP2R = "Fail";
            //if (FP1 < FHV || FP1 > FHL) FP1R = "Pass";
            //else FP1R = "Fail";
            //if (FP2 < FHV || FP2 > FHL) FP2R = "Pass";
            //else FP2R = "Fail";
            //if (HP1 < HHV || HP1 > HHL) HP1R = "Pass";
            //else HP1R = "Fail";
            //if (HP2 < HHV || FP2 > HHL) HP2R = "Pass";
            //else HP2R = "Fail";

            try
            {
                string TARContent = $"S{serialNumber}\r\n" +
                $"CDyson\r\n" +
                $"IDyson\r\n" +
                $"NJBL308CSNAP_JBL308CL100103\r\n" +
                $"PJBL308CSNAP\r\n" +
                $"n2\r\n" +
                $"OMachine3\r\n" +
                $"T{PassOrFail}\r\n" +
                $"[{DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss")}\r\n" +
                $"]{DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss")}\r\n" +
                $"MAttempsPower\r\n" +
                "@\r\n" +
                $"d{PowerP1B1}\r\n" +
                $"Umm\r\n" +
                $"q{PP1}\r\n" +
                "@\r\n" +
                $"MAttempsFlow\r\n" +
                "@\r\n" +
                $"d{PowerP2B2}\r\n" +
                $"Umm\r\n" +
                $"q{PP2}\r\n" +
                "@\r\n" +
                $"MAttempsHeat\r\n" +
                "@\r\n" +
                $"d{FlowP1B1}\r\n" +
                $"Umm\r\n" +
                $"q{FP1}\r\n" +  
                "@\r\n";


                // Path
                string LocalPath = string.Format(@"{0}\{1}_{2}.tar", "D:", serialNumber.Replace(':', '_'), "(" + DateTime.Now.ToString("MM-dd-yyyy hh-mm-ss") + ")");
                string MESPath = string.Format(@"{0}\{1}_{2}.tar", "Z:", serialNumber.Replace(':', '_'), "(" + DateTime.Now.ToString("MM-dd-yyyy hh-mm-ss") + ")");

                // Local Path
                if (!Directory.Exists("D:"))
                    Directory.CreateDirectory(Path.GetDirectoryName(LocalPath));
                bool bFileExists = File.Exists(LocalPath);
                if (!bFileExists)
                {
                    StreamWriter sw = new StreamWriter(LocalPath, false);
                    sw.Close();
                }

                File.WriteAllText(LocalPath, TARContent, Encoding.UTF8);

                // MES Path
                if (!Directory.Exists(Path.GetDirectoryName(MESPath)))
                    Directory.CreateDirectory(Path.GetDirectoryName(MESPath));
                bool bNetworkFileExists = File.Exists(MESPath);
                if (!bNetworkFileExists)
                {
                    StreamWriter sw = new StreamWriter(MESPath, false);
                    sw.Close();
                }
                File.WriteAllText(MESPath, TARContent, Encoding.UTF8);
                // File.WriteAllText(GetSettingValue("Path", "MESResult") + "\\MES\\TEST.tar", TARContent, Encoding.UTF8);
                return "Ok";
                

            }

            catch
            {
                return "Fail";
            }
        }



        private void button1_Click_1(object sender, EventArgs e)
        {
            DataSet.Tables[0].Rows[0]["Client"] = ClientTB.Text;
            DataSet.Tables[0].Rows[0]["Step"] = StepTB.Text;
            DataSet.Tables[0].Rows[0]["Machine"] = MachineTB.Text;
        }
    }
}
   