namespace MissionPlanner.GCSViews
{
    partial class Help
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

        #region Component Designer generated code

        /// <summary> 
        /// Required method for Designer support - do not modify 
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Help));
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.CHK_showconsole = new System.Windows.Forms.CheckBox();
            this.PIC_wizard = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.PIC_wizard)).BeginInit();
            this.SuspendLayout();
            // 
            // richTextBox1
            // 
            resources.ApplyResources(this.richTextBox1, "richTextBox1");
            this.richTextBox1.Cursor = System.Windows.Forms.Cursors.Default;
            this.richTextBox1.DetectUrls = false;
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.TextChanged += new System.EventHandler(this.richTextBox1_TextChanged);
            // 
            // CHK_showconsole
            // 
            resources.ApplyResources(this.CHK_showconsole, "CHK_showconsole");
            this.CHK_showconsole.Name = "CHK_showconsole";
            this.CHK_showconsole.UseVisualStyleBackColor = true;
            this.CHK_showconsole.CheckedChanged += new System.EventHandler(this.CHK_showconsole_CheckedChanged);
            // 
            // PIC_wizard
            // 
            resources.ApplyResources(this.PIC_wizard, "PIC_wizard");
            this.PIC_wizard.Image = global::MissionPlanner.Properties.Resources.wizardicon;
            this.PIC_wizard.Name = "PIC_wizard";
            this.PIC_wizard.TabStop = false;
            this.PIC_wizard.Click += new System.EventHandler(this.PIC_wizard_Click);
            // 
            // Help
            // 
            resources.ApplyResources(this, "$this");
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.PIC_wizard);
            this.Controls.Add(this.CHK_showconsole);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Help";
            this.Load += new System.EventHandler(this.Help_Load);
            ((System.ComponentModel.ISupportInitialize)(this.PIC_wizard)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.CheckBox CHK_showconsole;
        private System.Windows.Forms.PictureBox PIC_wizard;

    }
}
