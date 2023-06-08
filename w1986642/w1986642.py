# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1986642

# Date: 18/04/2023

# ---------------------------------------- Part 1,2,3 -----------------------------------------

credits_range = [0,20,40,60,80,100,120]
progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0

progress_list = []
trailer_list = []
retriever_list = []
excluded_list = []

def main_controller():
    answer = str(input("""Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: """))

    if answer.lower() == 'y':
        pass_credits_func()
    elif answer.lower() == 'q':
        print("\n--------------------------------------------------------------- \nHistogram")
        print(f"Progress {progress_count}   : {progress_count * '*'}")
        print(f"Trailer {trailer_count}    : {trailer_count * '*'}")
        print(f"Retriever {retriever_count}  : {retriever_count * '*'}")
        print(f"Excluded {excluded_count}   : {excluded_count * '*'}\n")
        print(f"{progress_count + trailer_count + retriever_count + excluded_count} outcomes in total.")
        print("---------------------------------------------------------------\n")

        input_list_func()


    else:
        print("Please enter only 'y' or 'q' to proceed\n")
        main_controller()

def pass_credits_func():
    try:
        global pass_credits
        pass_credits = int(input("Enter your PASS credits: "))

        if pass_credits in credits_range:
            defer_credits_func()
        else:
            print("Out of range\n")
            pass_credits_func()

    except ValueError:
        print("Integer required\n")
        pass_credits_func()

    return pass_credits

def defer_credits_func():
    try:
        global defer_credits
        defer_credits = int(input("Enter your DEFER credits: "))

        if defer_credits in credits_range:
            fail_credits_func()
        else:
            print("Out of range\n")
            defer_credits_func()

    except ValueError:
        print("Integer required\n")
        defer_credits_func()

    return defer_credits

def fail_credits_func():
    try:
        global progress_count, trailer_count ,retriever_count, excluded_count, progress_list, trailer_list, retriever_list, excluded_list

        fail_credits = int(input("Enter your FAIL credits: "))
        if fail_credits in credits_range:
            total_credits = pass_credits + defer_credits + fail_credits

            if total_credits == 120:
                if pass_credits == 120:
                   print("Progress\n")
                   progress_count += 1
                   progress_list.append((pass_credits,defer_credits,fail_credits))

                elif pass_credits == 100 and (defer_credits and fail_credits) <= 20:
                    print("Progress (module trailer)\n")
                    trailer_count += 1
                    trailer_list.append((pass_credits, defer_credits, fail_credits))

                elif (pass_credits == 40 and defer_credits == 0 and fail_credits == 80) or \
                        (pass_credits == 20 and defer_credits <= 20 and fail_credits >= 80) or \
                        (pass_credits == 0 and defer_credits <= 40 and fail_credits >= 80):
                    print("Exclude\n")
                    excluded_count += 1
                    excluded_list.append((pass_credits, defer_credits, fail_credits))

                else:
                    print("Module retriever\n")
                    retriever_count +=1
                    retriever_list.append((pass_credits, defer_credits, fail_credits))

                main_controller()
            else:
                print("Total incorrect, try again\n")
                pass_credits_func()

        else:
            print("Out of range\n")
            fail_credits_func()

    except ValueError:
        print("Integer required\n")
        fail_credits_func()

    return fail_credits, progress_list

def input_list_func():
    print("Part 2:\n")
    with open('Inputted_Progression_Data.txt','w') as file:

        for progress_items in progress_list:
            print("Progress - {}, {}, {}".format(*progress_items))
            file.write("Progress - {}, {}, {}\n".format(*progress_items))

        for trailer_items in trailer_list:
            print("Progress (module trailer) - {}, {}, {}".format(*trailer_items))
            file.write("Progress (module trailer) - {}, {}, {}\n".format(*trailer_items))

        for retriever_items in retriever_list:
            print("Module retriever - {}, {}, {}".format(*retriever_items))
            file.write("Module retriever - {}, {}, {}\n".format(*retriever_items))

        for exclude_items in excluded_list:
            print("Exclude - {}, {}, {}".format(*exclude_items))
            file.write("Exclude - {}, {}, {}\n".format(*exclude_items))

    print("\n---------------------------------------------------------------\n")
    print("Part 3:\n")
    with open('inputted_progression_data.txt') as file:
        print(file.read())

pass_credits_func()



# ---------------------------------------- Part 4 -----------------------------------------


# credits_range = [0,20,40,60,80,100,120]
# progress_count = 0
# trailer_count = 0
# retriever_count = 0
# excluded_count = 0
#
# data_dictionary = {}
#
# def main_controller():
#     answer = str(input("""Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: """))
#
#     if answer.lower() == 'y':
#         input_name()
#         pass_credits_func()
#     elif answer.lower() == 'q':
#         print("\n--------------------------------------------------------------- \nHistogram")
#         print(f"Progress {progress_count}   : {progress_count * '*'}")
#         print(f"Trailer {trailer_count}    : {trailer_count * '*'}")
#         print(f"Retriever {retriever_count}  : {retriever_count * '*'}")
#         print(f"Excluded {excluded_count}   : {excluded_count * '*'}\n")
#         print(f"{progress_count + trailer_count + retriever_count + excluded_count} outcomes in total.")
#         print("---------------------------------------------------------------\n")
#
#         dictionary_func()
#
#     else:
#         print("Please enter only 'y' or 'q' to proceed\n")
#         main_controller()
#
# def input_name():
#     global student_id
#     student_id = input("Enter your Student ID: ")
#     return student_id
#
# def pass_credits_func():
#     try:
#         global pass_credits
#         pass_credits = int(input("Enter your PASS credits: "))
#
#         if pass_credits in credits_range:
#             defer_credits_func()
#         else:
#             print("Out of range\n")
#             pass_credits_func()
#
#     except ValueError:
#         print("Integer required\n")
#         pass_credits_func()
#
#     return pass_credits
#
# def defer_credits_func():
#     try:
#         global defer_credits
#         defer_credits = int(input("Enter your DEFER credits: "))
#
#         if defer_credits in credits_range:
#             fail_credits_func()
#         else:
#             print("Out of range\n")
#             defer_credits_func()
#
#     except ValueError:
#         print("Integer required\n")
#         defer_credits_func()
#
#     return defer_credits
#
# def fail_credits_func():
#     try:
#         global progress_count, trailer_count ,retriever_count, excluded_count
#
#         fail_credits = int(input("Enter your FAIL credits: "))
#         if fail_credits in credits_range:
#             total_credits = pass_credits + defer_credits + fail_credits
#
#             if total_credits == 120:
#                 if pass_credits == 120:
#                    print("Progress\n")
#                    progress_count += 1
#                    data_dictionary[student_id]  = "Progress", pass_credits, defer_credits, fail_credits
#
#                 elif pass_credits == 100 and (defer_credits and fail_credits) <= 20:
#                     print("Progress (module trailer)\n")
#                     trailer_count += 1
#                     data_dictionary[student_id]  = "Progress (module trailer)", pass_credits, defer_credits, fail_credits
#
#                 elif (pass_credits == 40 and defer_credits == 0 and fail_credits == 80) or \
#                         (pass_credits == 20 and defer_credits <= 20 and fail_credits >= 80) or \
#                         (pass_credits == 0 and defer_credits <= 40 and fail_credits >= 80):
#                     print("Exclude\n")
#                     excluded_count += 1
#                     data_dictionary[student_id]  = "Exclude", pass_credits, defer_credits, fail_credits
#
#                 else:
#                     print("Module retriever\n")
#                     retriever_count +=1
#                     data_dictionary[student_id]  = "Module retriever", pass_credits, defer_credits, fail_credits
#
#                 main_controller()
#             else:
#                 print("Total incorrect, try again\n")
#                 pass_credits_func()
#
#         else:
#             print("Out of range\n")
#             fail_credits_func()
#
#     except ValueError:
#         print("Integer required\n")
#         fail_credits_func()
#
#     return fail_credits
#
# def dictionary_func():
#     print("Part 4:\n")
#
#     for key, value in data_dictionary.items():
#         print("{} : {} - {}, {}, {}".format(key, value[0], value[1], value[2], value[3]),end=' ')
#
# input_name()
# pass_credits_func()