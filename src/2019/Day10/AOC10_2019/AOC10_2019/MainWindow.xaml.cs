using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Runtime.Remoting.Channels;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Timer = System.Timers.Timer;

namespace AOC10_2019
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            
        }

        private int gridSpacing = 30;
        private int gridSize = 30;
        
        private int dotSize = 4;
        readonly Dictionary<(int, int), List<(int,int)>> _pythonOutput = new Dictionary<(int, int), List<(int, int)>>();
        readonly List<(int,int)> _keys = new List<(int, int)>();
        readonly Dictionary<(int, int,int,int), bool> lineStates = new Dictionary<(int, int,int,int), bool>();
        private int _lineIndex = 0;
        private bool _keyMode = false;
        private int _keyIndex = 0;
        private (int, int) _specificKey = (1,0);
        private BitmapImage ast = null;

        Timer timer = new Timer(1);

        private void MainWindow_OnLoaded(object sender, RoutedEventArgs e)
        {
        
            timer.Elapsed += Timer_Elapsed;
         
            
            ast = new BitmapImage();
            ast.BeginInit();
            ast.UriSource = new Uri(@"C:\Dropbox\Github\AdventOfPython\src\2019\Day10\AOC10_2019\AOC10_2019\asteroid.png");
            ast.EndInit();
            

            string fileName = @"C:\Dropbox\Github\AdventOfPython\src\2019\day10\Day10.py";
            string intputPath = "";
            Process p = new Process();
            p.StartInfo = new ProcessStartInfo(@"C:\Users\Alexsdesktop\AppData\Local\Microsoft\WindowsApps\python3.8.exe", fileName)
            {
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };
            p.Start();
            intputPath = p.StandardOutput.ReadLine();
            while (!p.StandardOutput.EndOfStream)
            {
                 var output = p.StandardOutput.ReadLine();
                 if (string.IsNullOrWhiteSpace(output)  || !output.Contains(","))continue;
                 ;
                 var key = new ValueTuple<int,int>(int.Parse(output.Split(',')[0].Split('-')[0]), int.Parse(output.Split(',')[0].Split('-')[1]));
                 var values = (int.Parse(output.Split(',')[1]), int.Parse(output.Split(',')[2]));
                 lineStates[(key.Item1,key.Item2,values.Item1,values.Item2)] = output.Split(',')[3] == "1";
                 if (!_pythonOutput.ContainsKey(key))
                 {
                    _pythonOutput[key] = new List<(int, int)>();
                 }
                 _pythonOutput[key].Add(values);
                 if (!_keys.Contains(key))
                    _keys.Add(key);
            }


            p.WaitForExit();

 //Console.WriteLine(output);

 Console.ReadLine();

            foreach (var asteroid in File.ReadAllLines(intputPath))
            {
                asteroids.Add(asteroid.Select(b => b != '.').ToList());
            }

            gridSize = asteroids.Count;
           
            for (var index = 0; index < asteroids.Count; index++)
            {
                var asteroid = asteroids[index];
                for (var i = 0; i < asteroid.Count; i++)
                {
                    if (asteroid[i])
                        DrawAsteroid( i,index);

                }
            }

            for (int x = 0; x < gridSize; x++)
            {
                for (int y = 0; y < gridSize; y++)
                {

                    //DrawPoint(x, y);
                }
            }

            _specificKey = _keys[_keyIndex];
            //DrawLines();
          

        }

        private void Timer_Elapsed(object sender, System.Timers.ElapsedEventArgs e)
        {
            if (_lineIndex >= _pythonOutput[_specificKey].Count-1)
            {
                _lineIndex = 0;
                _keyIndex++;
                _specificKey = _keys[_keyIndex];
                Application.Current.Dispatcher.Invoke(new Action(() => { DrawLines(true); }));
                counter = 0;
            }
            else
                _lineIndex++;

            Application.Current.Dispatcher.Invoke(new Action(() => { DrawLines(false); }));
        }

        private void DrawLines(bool clearLines)
        {
            if(clearLines)
            {
                lines.ForEach(Canvas.Children.Remove);
                lines.Clear();
            }
            if (_keyMode)
            {
                for (var y = 0; y < asteroids.Count; y++)
                {
                    var asteroid = asteroids[y];
                    for (var x = 0; x < asteroid.Count; x++)
                    {
                        bool isGreen = _pythonOutput[_keys[_keyIndex]].Contains((x, y));
                        var x2 = _keys[_keyIndex].Item1;
                        var y2 = _keys[_keyIndex].Item2;
                        if (x2 == x && y2 == y)
                            continue;
                        if (asteroid[x])
                            DrawLine(x2, y2, x, y, isGreen);
                    }
                }
            }
            else
            {
                var x2 = _pythonOutput[_specificKey][_lineIndex].Item1;
                var y2 = _pythonOutput[_specificKey][_lineIndex].Item2;
                DrawLine(x2, y2, _specificKey.Item1, _specificKey.Item2, true);
            }
        }

        private List<List<bool>> asteroids = new List<List<bool>>();

        List<Line> lines = new List<Line>();
        private int counter = 0;
        private void DrawLine(int x, int y, int x2, int y2,bool isGreen)
        {

            points.ForEach(Canvas.Children.Remove);
            points.Clear();
            DrawPoint(x, y);
            DrawPoint(x2,y2);
            var padding = dotSize * 1.25;
            var line = new Line();
            line.Stroke = lineStates[(x,y,x2,y2)]? Brushes.Red: Brushes.Green;
            Canvas.SetZIndex(line, 5);
            //Canvas.SetZIndex(line, lineStates[(x, y, x2, y2)] ? 4 : 5);
            if (!lineStates[(x, y, x2, y2)])
            {
                counter ++ ;
                LAbelCords.Content = counter;
            }
            
            line.X1 = x * gridSpacing  + padding;
            line.X2 = x2 * gridSpacing + padding;
            line.Y1 = y* gridSpacing + padding;
            line.Y2 = y2 * gridSpacing + padding;

            line.StrokeThickness = 3;
            Canvas.Children.Add(line);
            lines.Add(line);
        }
        private void DrawPoint(int x, int y)
        {
            var padding = dotSize * 1.25;

            Ellipse currentDot = new Ellipse();
            currentDot.Stroke = new SolidColorBrush(Colors.Blue);
            currentDot.StrokeThickness = 5;
            Canvas.SetZIndex(currentDot, 53);
            currentDot.Height = dotSize;
            currentDot.Width = dotSize;
            currentDot.Fill = new SolidColorBrush(Colors.Blue);
            currentDot.Margin = new Thickness(x*gridSpacing-(dotSize / 2) + padding, y*gridSpacing - (dotSize / 2)+ padding, 0, 0); // Sets the position.
            Canvas.Children.Add(currentDot);
            points.Add(currentDot);
           
        }
        List<Ellipse> points = new List<Ellipse>();
        private void DrawAsteroid(int x, int y)
        {
            var padding = dotSize * 1.25;
            int mult = 6;
            Image currentDot = new Image();
            //currentDot.Stroke = new SolidColorBrush(Colors.Red);
            //currentDot.StrokeThickness = 5;
// image.Source = new BitmapImage(new Uri(AppDomain.CurrentDomain.BaseDirectory + "image.png", UriKind.Absolute));
            currentDot.Source = ast;
            Canvas.SetZIndex(currentDot, 2);
            currentDot.Height = dotSize* mult;
            currentDot.Width = dotSize* mult;
            currentDot.Tag = $"{x},{y}";
            currentDot.MouseEnter += (sender, args) => { LAbelCords.Content = (sender as Image)?.Tag; } ;
            currentDot.MouseDown += (sender, args) =>
            {
                var tag = (sender as Image)?.Tag.ToString();
                _specificKey = (int.Parse(tag.Split(',')[0]), int.Parse(tag.Split(',')[1]));
                _keyIndex = 0;
                _lineIndex = 0;
                //DrawLines(false);

            };
// currentDot.Fill = new SolidColorBrush(Colors.Red);
            currentDot.Margin = new Thickness(x*gridSpacing - (dotSize* mult / 2) + padding , y*gridSpacing - (dotSize* mult / 2) + padding, 0, 0); // Sets the position.
            Canvas.Children.Add(currentDot);
        }

        private void ButtonBase_OnClick(object sender, RoutedEventArgs e)
        {
            timer.Start();
            return;
            Application.Current.Dispatcher.Invoke(new Action(() =>
            {
                _keyIndex++;
                _lineIndex++;
                //DrawLines();
            }));
        }
    }
}
