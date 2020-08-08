def main():
    data = ("self", "py", 1.543)
    format_string = "Hello"
    print("{0} {1[0]}.{1[1]} learner, you have only {1[2]:0.1f} units left before you master the course!"
          .format(format_string, data))


if __name__ == '__main__':
    main()
