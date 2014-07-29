::############################################################
::Test plotPerformanceLogs.py

::python plotPerformanceLogs.py

::python plotPerformanceLogs.py -output LogPlot2.png

::python plotPerformanceLogs.py -output LogPlot3.png ../data/results_firstrun.txt

::python plotPerformanceLogs.py -output LogPlot4.png ../data/results_firstrun.txt ../data/results_secondrun.txt ../data/results_baseline.txt

::python plotMemoryLogs.py --help

::python plotMemoryLogs.py

::python plotMemoryLogs.py -output MemLog2.png

::python plotMemoryLogs.py -output MemLog3.png -logFile1 ..\data\PerfLog_feature_OFF.txt -logFile2 ..\data\PerfLog_feature_ON.txt

::del *.png

::pause
::############################################################


::############################################################
::Test installCheck.py
set SCRIPT=installCheck.py

::python %SCRIPT%

::python %SCRIPT% --help

::python %SCRIPT% -installer installer-11.2.3-vc10x64-19983.exe

::python %SCRIPT% -installer installer-11.2.3-vc10x64-19983.exe -installDir C:\objy -repeat 1 -osString win

::python %SCRIPT% -installer "C:\Users\cuongd\Downloads\temp\installer-11.2.3-vc10x64-19983.exe" -installDir C:\objy -repeat 0 -osString win

python %SCRIPT% -installer "C:\Users\cuongd\Downloads\temp\installer-11.2.3-vc10x64-19983.exe" -installDir C:\objy -repeat 0 -osString win

::pause
::############################################################