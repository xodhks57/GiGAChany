using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Gigachany_2ndWeekUI
{
    public partial class Form1_Main : Form
    {
        Point fPt;
        bool isMove;
        bool isGraph;
        bool isImage;

        public Form1_Main()
        {
            InitializeComponent();
        }
        
        #region * ButtonControls
        private void Button1_Click(object sender, EventArgs e) // 이미지 불러오기 버튼
        {
            openFileDialog1.Filter = "이미지 파일(.jpg)|*.jpg|모든 파일(*.*)|*.*";
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
            }
        }

        private void Button4_Click(object sender, EventArgs e) // 초기화 버튼
        {
            pictureBox1.Image = new Bitmap(Properties.Resources.man);
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
