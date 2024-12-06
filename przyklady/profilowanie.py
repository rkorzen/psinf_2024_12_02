# import cProfile
# import pstats

# def slow_function():
#     result = ""
#     for i in range(10**6):
#         result += str(i ** 2)
#     return result

# if __name__ == "__main__":
#     profiler = cProfile.Profile()
#     profiler.enable()
#     slow_function()
#     profiler.disable()
#     stats = pstats.Stats(profiler)
#     stats.strip_dirs()  # Usuwa pełne ścieżki do plików, dla czytelności
#     stats.sort_stats('time').print_stats(20)  # Sortowanie po czasie


# import profile

# def slow_function():
#     result = ""
#     for i in range(10**6):
#         result += str(i ** 2)
#     return result

# if __name__ == "__main__":
#     profile.run("slow_function()")



from line_profiler import LineProfiler

def slow_function():
    result = ""
    for i in range(10**6):
        result += str(i ** 2)
    return result

def slow_function_optimized():
    result = (str(i ** 2) for i in range(10**6))
    return "".join(result)

if __name__ == "__main__":
    profiler = LineProfiler()
    profiler.add_function(slow_function)
    profiler.add_function(slow_function_optimized)
    profiler.enable()
    slow_function()
    slow_function_optimized()
    profiler.disable()
    profiler.print_stats()
