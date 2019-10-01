using System;
using System.Drawing;
using System.Windows.Forms;

namespace Gigachany_2ndWeekUI
{
    public partial class Form1_Main : Form
    {
        Point fPt;
        bool isMove;
        bool isGraph = false;
        bool isImage = false;
        

        public Form1_Main()
        {
            InitializeComponent();
			Graph.Titles.Add("얼굴 표정 차트").Font = new Font("나눔스퀘어", 18F, FontStyle.Bold);
			Graph.Series["표정"].Points.Clear();
			Graph.Series["표정"].Points.AddXY("행복", 100);
			Graph.Series["표정"].Points.AddXY("분노", 80);
			Graph.Series["표정"].Points.AddXY("슬픔", 40);
			Graph.Series["표정"].Points.AddXY("무표정", 60);
			Graph.Series["표정"].Points[0].Color = Color.FromArgb(236, 120, 121);
			Graph.Series["표정"].Points[1].Color = Color.FromArgb(136, 182, 191);
			Graph.Series["표정"].Points[2].Color = Color.FromArgb(236, 120, 121);
		}
        
        #region * ButtonControls
        private void Button1_Click(object sender, EventArgs e) // 이미지 불러오기 버튼
        {
            openFileDialog1.Filter = "이미지 파일(.jpg)|*.jpg";
            openFileDialog1.Title = "이미지 불러오기";
            openFileDialog1.FileName = "";
            openFileDialog1.ShowDialog();
            if (openFileDialog1.FileName != "")
            {
                pictureBox1.Image = new Bitmap(openFileDialog1.FileName);
                isImage = true;
            }
        }

        private void Button2_Click(object sender, EventArgs e) // 판별 시작 버튼
        {
			if (isImage == true)
            {
                Form2_Result F2 = new Form2_Result();
                F2.Show();
            }
            else MessageBox.Show("불러온 이미지가 없습니다!");
        }

        private void Button3_Click(object sender, EventArgs e) // 그래프 출력 버튼
        {
            if (isGraph == false)
            {
                this.SetClientSizeCore(950, 610);
                isGraph = true;
            }
            else if (isGraph == true)
            {
                this.SetClientSizeCore(475, 610);
                isGraph = false;
                MessageBox.Show("불러온 이미지가 없습니다!");
            } 

            
        }

        private void Button3_Click(object sender, EventArgs e) // 그래프 출력 버튼
        {
            Form3_ScreenShot F3 = new Form3_ScreenShot();
            F3.Show();
        }

        private void Button4_Click(object sender, EventArgs e) // 초기화 버튼
        {
            isImage = false;
            this.SetClientSizeCore(474, 610);
            pictureBox1.Image = new Bitmap(Properties.Resources.Q);
        }
        
        private void Button5_Click(object sender, EventArgs e) // 종료 버튼
        {
            this.Close();
        }
        #endregion

        #region * MouseControls
        private void panel1_MouseDown(object sender, MouseEventArgs e)
        {
            isMove = true;
            fPt = new Point(e.X, e.Y);
        }

        private void panel1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMove && (e.Button & MouseButtons.Left) == MouseButtons.Left)
            {
                Location = new Point(this.Left - (fPt.X - e.X), this.Top - (fPt.Y - e.Y));
            }
        }

        private void panel1_MouseUp(object sender, MouseEventArgs e)
        {
            isMove = false;
        }
        #endregion

    }
}
