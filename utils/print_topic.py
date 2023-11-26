import calculate_time


def init(topic):
    print("\n")
    print(
        "============================================================================="
    )
    print(topic)
    calculate_time.init()


def finish_default():
    calculate_time.finish()
    print(
        "-----------------------------------------------------------------------------"
    )
    execution_time = calculate_time.get()
    print("✅ Concluído com sucesso \n🕛", execution_time)
    print(
        "============================================================================="
    )
    return execution_time


def finish_variation():
    calculate_time.finish()
    print(
        "-----------------------------------------------------------------------------"
    )
    print("✅ Concluído com sucesso \n🕛", calculate_time.get())
