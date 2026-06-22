'''
A company stores server logs in a files:
write a python program:
1.read log.txt:
2.count:
total lines
Error messages
Warning messages
Info Messages
display analysis report

'''
class LogAnalyzer:
    def analyze_log(self):
        try:
            with open("log.txt", "r") as file:
                lines = file.readlines()

                error_count = 0
                warning_count = 0
                info_count = 0

            for line in lines:
                if "ERROR" in line:
                    error_count += 1
                elif "WARNING" in line:
                    warning_count += 1
                elif "INFO" in line:
                    info_count += 1
            print("Log Report")
            print(
                "Totallines:",len(lines)
            )
            print(error_count)
            print(info_count)
            print(warning_count)
        except FileNotFoundError as e:
            print(e)

obj = LogAnalyzer()
obj.analyze_log()
