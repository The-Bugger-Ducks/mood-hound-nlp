from utils.calculate_time import init, finish, get


def init_topic(topic):
    print("\n")
    print(
        "============================================================================="
    )
    print(topic)
    init()


def finish_topic_default():
    finish()
    print(
        "-----------------------------------------------------------------------------"
    )
    execution_time = get()
    print("✅ Concluído com sucesso \n🕛", execution_time)
    print(
        "============================================================================="
    )
    return execution_time
