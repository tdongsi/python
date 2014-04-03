::Test plotPerformanceLogs.py
::TODO: A unittest module is better

python plotPerformanceLogs.py

python plotPerformanceLogs.py -output LogPlot2.png

python plotPerformanceLogs.py -output LogPlot3.png ../data/results_firstrun.txt

python plotPerformanceLogs.py -output LogPlot4.png ../data/results_firstrun.txt ../data/results_secondrun.txt ../data/results_baseline.txt

python plotMemoryLogs.py --help

python plotMemoryLogs.py

python plotMemoryLogs.py -output MemLog2.png

python plotMemoryLogs.py -output MemLog3.png -logFile1 ..\data\PerfLog_feature_OFF.txt -logFile2 ..\data\PerfLog_feature_ON.txt

del *.png

pause