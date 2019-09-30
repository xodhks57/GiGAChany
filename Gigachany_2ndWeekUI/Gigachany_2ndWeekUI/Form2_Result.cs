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
    public partial class Form2_Result : Form
    {
        Point fPt;
        bool isMove;

        public Form2_Result()
        {
            InitializeComponent();
        }
        
        #region * ButtonControls

        private void Button1_Click(object sender, EventArgs e) // 닫기 버튼
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
