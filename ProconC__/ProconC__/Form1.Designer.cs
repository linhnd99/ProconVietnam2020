namespace ProconC__
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.txtToken = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.btnGetMatches = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.txtMatchID = new System.Windows.Forms.TextBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.txtAllMatch = new System.Windows.Forms.TextBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.txtActionTurn = new System.Windows.Forms.TextBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.lblMatchID = new System.Windows.Forms.Label();
            this.lblNameMatch = new System.Windows.Forms.Label();
            this.lblTurn = new System.Windows.Forms.Label();
            this.txtAPIURL = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.txtTimeLoop = new System.Windows.Forms.TextBox();
            this.btnGetMatch = new System.Windows.Forms.Button();
            this.btnSendAction = new System.Windows.Forms.Button();
            this.btnAutoPlay = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.SuspendLayout();
            // 
            // txtToken
            // 
            this.txtToken.Location = new System.Drawing.Point(65, 42);
            this.txtToken.Name = "txtToken";
            this.txtToken.Size = new System.Drawing.Size(349, 20);
            this.txtToken.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 45);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(38, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Token";
            // 
            // btnGetMatches
            // 
            this.btnGetMatches.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnGetMatches.Location = new System.Drawing.Point(15, 111);
            this.btnGetMatches.Name = "btnGetMatches";
            this.btnGetMatches.Size = new System.Drawing.Size(114, 32);
            this.btnGetMatches.TabIndex = 3;
            this.btnGetMatches.Text = "Get matches";
            this.btnGetMatches.UseVisualStyleBackColor = true;
            this.btnGetMatches.Click += new System.EventHandler(this.btnGetMatches_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 77);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(51, 13);
            this.label2.TabIndex = 5;
            this.label2.Text = "Match ID";
            // 
            // txtMatchID
            // 
            this.txtMatchID.Location = new System.Drawing.Point(65, 74);
            this.txtMatchID.Name = "txtMatchID";
            this.txtMatchID.Size = new System.Drawing.Size(64, 20);
            this.txtMatchID.TabIndex = 4;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.txtAllMatch);
            this.groupBox1.Location = new System.Drawing.Point(8, 151);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(415, 466);
            this.groupBox1.TabIndex = 6;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "All match info";
            // 
            // txtAllMatch
            // 
            this.txtAllMatch.Location = new System.Drawing.Point(7, 31);
            this.txtAllMatch.Multiline = true;
            this.txtAllMatch.Name = "txtAllMatch";
            this.txtAllMatch.Size = new System.Drawing.Size(399, 415);
            this.txtAllMatch.TabIndex = 0;
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.txtActionTurn);
            this.groupBox2.Location = new System.Drawing.Point(439, 151);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(415, 466);
            this.groupBox2.TabIndex = 7;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Action Turn";
            // 
            // txtActionTurn
            // 
            this.txtActionTurn.Location = new System.Drawing.Point(7, 31);
            this.txtActionTurn.Multiline = true;
            this.txtActionTurn.Name = "txtActionTurn";
            this.txtActionTurn.Size = new System.Drawing.Size(399, 415);
            this.txtActionTurn.TabIndex = 0;
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.lblTurn);
            this.groupBox3.Controls.Add(this.lblNameMatch);
            this.groupBox3.Controls.Add(this.lblMatchID);
            this.groupBox3.Location = new System.Drawing.Point(444, 19);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(410, 124);
            this.groupBox3.TabIndex = 8;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Match Info";
            // 
            // lblMatchID
            // 
            this.lblMatchID.AutoSize = true;
            this.lblMatchID.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblMatchID.Location = new System.Drawing.Point(17, 26);
            this.lblMatchID.Name = "lblMatchID";
            this.lblMatchID.Size = new System.Drawing.Size(78, 20);
            this.lblMatchID.TabIndex = 0;
            this.lblMatchID.Text = "Match ID:";
            // 
            // lblNameMatch
            // 
            this.lblNameMatch.AutoSize = true;
            this.lblNameMatch.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblNameMatch.Location = new System.Drawing.Point(17, 59);
            this.lblNameMatch.Name = "lblNameMatch";
            this.lblNameMatch.Size = new System.Drawing.Size(103, 20);
            this.lblNameMatch.TabIndex = 1;
            this.lblNameMatch.Text = "Name match:";
            // 
            // lblTurn
            // 
            this.lblTurn.AutoSize = true;
            this.lblTurn.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblTurn.Location = new System.Drawing.Point(17, 90);
            this.lblTurn.Name = "lblTurn";
            this.lblTurn.Size = new System.Drawing.Size(50, 20);
            this.lblTurn.TabIndex = 2;
            this.lblTurn.Text = "Turn:";
            // 
            // txtAPIURL
            // 
            this.txtAPIURL.Location = new System.Drawing.Point(65, 16);
            this.txtAPIURL.Name = "txtAPIURL";
            this.txtAPIURL.Size = new System.Drawing.Size(349, 20);
            this.txtAPIURL.TabIndex = 9;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(12, 19);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(49, 13);
            this.label6.TabIndex = 10;
            this.label6.Text = "API URL";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(154, 78);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(53, 13);
            this.label7.TabIndex = 12;
            this.label7.Text = "Time loop";
            // 
            // txtTimeLoop
            // 
            this.txtTimeLoop.Location = new System.Drawing.Point(207, 75);
            this.txtTimeLoop.Name = "txtTimeLoop";
            this.txtTimeLoop.Size = new System.Drawing.Size(64, 20);
            this.txtTimeLoop.TabIndex = 11;
            this.txtTimeLoop.TextChanged += new System.EventHandler(this.textBox6_TextChanged);
            // 
            // btnGetMatch
            // 
            this.btnGetMatch.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnGetMatch.Location = new System.Drawing.Point(157, 109);
            this.btnGetMatch.Name = "btnGetMatch";
            this.btnGetMatch.Size = new System.Drawing.Size(114, 32);
            this.btnGetMatch.TabIndex = 13;
            this.btnGetMatch.Text = "Get match";
            this.btnGetMatch.UseVisualStyleBackColor = true;
            // 
            // btnSendAction
            // 
            this.btnSendAction.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnSendAction.Location = new System.Drawing.Point(300, 109);
            this.btnSendAction.Name = "btnSendAction";
            this.btnSendAction.Size = new System.Drawing.Size(114, 32);
            this.btnSendAction.TabIndex = 14;
            this.btnSendAction.Text = "Send action";
            this.btnSendAction.UseVisualStyleBackColor = true;
            // 
            // btnAutoPlay
            // 
            this.btnAutoPlay.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnAutoPlay.Location = new System.Drawing.Point(300, 71);
            this.btnAutoPlay.Name = "btnAutoPlay";
            this.btnAutoPlay.Size = new System.Drawing.Size(114, 32);
            this.btnAutoPlay.TabIndex = 15;
            this.btnAutoPlay.Text = "Auto play";
            this.btnAutoPlay.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(886, 642);
            this.Controls.Add(this.btnAutoPlay);
            this.Controls.Add(this.btnSendAction);
            this.Controls.Add(this.btnGetMatch);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.txtTimeLoop);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.txtAPIURL);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtMatchID);
            this.Controls.Add(this.btnGetMatches);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txtToken);
            this.Name = "Form1";
            this.Text = "Procon 2020";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtToken;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnGetMatches;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txtMatchID;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox txtAllMatch;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.TextBox txtActionTurn;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Label lblTurn;
        private System.Windows.Forms.Label lblNameMatch;
        private System.Windows.Forms.Label lblMatchID;
        private System.Windows.Forms.TextBox txtAPIURL;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox txtTimeLoop;
        private System.Windows.Forms.Button btnGetMatch;
        private System.Windows.Forms.Button btnSendAction;
        private System.Windows.Forms.Button btnAutoPlay;
    }
}

