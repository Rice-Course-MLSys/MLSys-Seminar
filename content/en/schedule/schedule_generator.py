from datetime import datetime, timedelta

def format_date(dt: datetime) -> str:
    return dt.strftime("%b %d").lstrip("0").replace(" 0", " ")

def format_time_range(start_hour: int, start_minute: int, duration_min: int) -> str:
    start = datetime(2000, 1, 1, start_hour, start_minute) 
    end = start + timedelta(minutes=duration_min)
    return f"{start.strftime('%I:%M %p').lstrip('0')}–{end.strftime('%I:%M %p').lstrip('0')}"

def generate_schedule(
        first_lecture_date: str, 
        chapters: dict, 
        start_hour: int = 15, 
        start_minute: int = 0, 
        duration_min: int = 75
    ) -> str:

    date = datetime.strptime(first_lecture_date, "%Y-%m-%d")
    first_date = date

    time_str = format_time_range(start_hour, start_minute, duration_min)
    
    md = "---\ntitle: Schedule\n---\n\n--- \n"
    md += "| Date   | Lecture | Logistics |\n"
    md += "|--------|---------|-----------|\n"

    lecture_index = 1

    md += f"| {format_date(date)} ({time_str}) | Lecture {lecture_index}: **Introduction**<br>[[Slides]](https://github.com/Rice-Course-MLSys/MLSys-Seminar/tree/main/) [[Video]](https://github.com/Rice-Course-MLSys/MLSys-Seminar/tree/main/) | |\n"
    lecture_index += 1

    while date.weekday() != 4:  # 4 = Friday
        date += timedelta(days=1)
    
    if first_date == date:
        date += timedelta(days=7)

    for chapter_name, lectures in chapters.items():
        md += f"| | **{chapter_name}** | |\n"
        for lec in lectures:
            md += f"| {format_date(date)} ({time_str}) | Lecture {lecture_index}: **{lec}**<br>[Slides] [Video] [Video (Live)] | |\n"
            lecture_index += 1
            date += timedelta(days=7)

    return md

chapters = {
    "Chapter I: Kernel Related": [
        "I/O Aware & Exact Attention",
        "Sparse Attention",
        "Kernel Generation & Compiler",
        "Execution Optimization/Serving"
    ],
    "Chapter II: Efficient LLM": [
        "LLM 101",
        "Efficient Inference & Long-context",
        "Model Compression (Quant & Pruning)", 
        "Efficient Training",
        "Efficient Model Designs"
    ],
    "Chapter III: Video Generation": [
        "SOTA/Baseline Model",
        "Optimization Techniques",
        "Long Video Generation",
        "Video Super Resolution"
    ],
    "Chapter IV: Secure LLM": [
        "Diffusion Model/Flow Matching",
        "Watermarking",
        "Efficient CNN", 
        "Encryption"
    ],
    "Chapter V: MLLM Video Understanding": [
        "SOTA/Baseline",
        "Optimization Techniques",
        "Algorithm Design"
    ]

}

md_content = generate_schedule("2025-09-05", chapters)
print(md_content)
