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
    print("✅ Concluído com sucesso \n🕛", get())
    print(
        "============================================================================="
    )
