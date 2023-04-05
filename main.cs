namespace mainApp
{
    using System;
    using System.IO;
    using System.Net;
    using System.Net.Http;
    using NewtonSoft.Json;
    using Newtonsoft.Json.Linq;

    public static class mainEnv
    {
        public static void Load(string filePath)
        {
            if (!File.Exists(filePath))
                return;

            foreach (var line in File.ReadAllLines(filePath))
            {
                var parts = line.Split('=', StringSplitOptions.RemoveEmptyEntries);

                if (parts.Length != 2)
                    continue;

                Environment.SetEnvironmentVariable(parts[0], parts[1]);
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var root = Directory.GetCurrentDirectory();
            var dotenv = Path.Combine(root, ".env");
        
            mainEnv.Load(dotenv);

            var personalAccessToken = Environment.GetEnvironmentVariable("AZURE_DEVOPS_PERSONAL_ACCESS_TOKEN");
            var workitem_revisions_url = Environment.GetEnvironmentVariable("AZURE_DEVOPS_WORK_ITEM_REVISIONS_URL");
            
            Console.WriteLine("Hello World!");

            using (var client = new HttpClient()) {
                client.DefaultRequestHeaders.Accept.Clear();
                client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
                client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Basic", Convert.ToBase64String(System.Text.Encoding.ASCII.GetBytes(string.Format("{0}:{1}", "", personalAccessToken))));
                
                var response = client.GetAsync(workitem_revisions_url).Result;

                if (response.IsSuccessStatusCode)
                {
                    var revisionsJson = response.Content.ReadAsStringAsync().Result;
                    JObject revisions = JsonConvert.DeserializeObject<JObject>(revisionsJson);
                
                    foreach (JToken revision in revisions["value"]) {
                        string revisionId = (string)revision["id"];
                        int revisionNumber = (int)revision["rev"];

                        JObject fields = (JObject)revision["fields"];

                        string workItemId = (string)fields["System.Id"];
                        string title = (string)fields["System.Title"];
                        string state = (string)fields["System.State"];
                    }
                }
                else
                {
                    Console.WriteLine("{0} ({1})", (int)response.StatusCode, response.ReasonPhrase);
                }
            }
        }
    }
}