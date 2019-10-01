using System;
using System.Drawing;
using System.Windows.Forms;

namespace Gigachany_2ndWeekUI
{
    public partial class Form3_ScreenShot : Form
    {
        Point fPt;
        bool isMove;
        bool isScreenShot = false;

        public Form3_ScreenShot()
        {
            InitializeComponent();
        }
        
        #region * ButtonControls
        private void Button1_Click(object sender, EventArgs e) // 닫기 버튼
        {
            this.Close();
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            Bitmap b = new Bitmap(this.pictureBox1.Width, this.pictureBox1.Height);
            Graphics g = Graphics.FromImage(b);
            g.CopyFromScreen(PointToScreen(new Point(this.pictureBox1.Location.X, this.pictureBox1.Location.Y)), new Point(0, 0), this.pictureBox1.Size);
            b.Save("ScreenShot.jpg");
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
