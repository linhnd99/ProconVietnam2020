using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ProconC__
{
    public partial class Form1 : Form
    {
        private string apiurl;
        private string token;
        HttpClient client;
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {

        }


        private void btnGetMatches_Click(object sender, EventArgs e)
        {
            Dictionary<string, dynamic> matches = GetMatchesAsync().Result;
            matches
        }

        private void CreateRequest()
        {
            apiurl = txtAPIURL.Text;
            token = txtToken.Text;
            client = new HttpClient();
            client.BaseAddress = new Uri(apiurl);
            client.DefaultRequestHeaders.Clear();
            client.DefaultRequestHeaders.Add("Authorization", token);
            client.DefaultRequestHeaders.Add("Content-Type", "application/json");
        }
        async Task<Dictionary<string,dynamic>> GetMatchesAsync()
        {
            CreateRequest();
            HttpResponseMessage response = await client.GetAsync("matches");
            if (response.IsSuccessStatusCode)
            {
                var res = await response.Content.ReadAsStringAsync();
                return JsonConvert.DeserializeObject<Dictionary<string,dynamic>>(res);
            }
            else
            {
                Console.WriteLine("Post failed: " + response.ToString());
                MessageBox.Show(response.StatusCode.ToString());
            }
            return null;
        }

        async Task<Dictionary<string,dynamic>> GetMatch()
        {
            CreateRequest();
            HttpResponseMessage response = await client.GetAsync($"match/{txtMatchID.Text}");
            if (response.IsSuccessStatusCode)
            {
                var res = await response.Content.ReadAsStringAsync();
                return JsonConvert.DeserializeObject<Dictionary<string, dynamic>>(res);
            }
            else
            {
                Console.WriteLine("Post failed: " + response.ToString());
                MessageBox.Show(response.StatusCode.ToString());
            }
            return null;
        }

        async Task PostAction(Dictionary<string,dynamic> data)
        {
            CreateRequest();
            HttpResponseMessage response = await client.PostAsJsonAsync($"match/{txtMatchID.Text}",data);
            if (response.IsSuccessStatusCode)
            {
                Console.WriteLine("Post success");
                txtActionTurn.Text = JsonConvert.SerializeObject(data,Formatting.Indented);
            }
            else
            {
                Console.WriteLine("Post failed: " + response.ToString());
                MessageBox.Show(response.StatusCode.ToString());
            }
        }
    }
}
