from config2 import Config


def select_models(task: str):

    # TBD: This function selects the primary and fallback models based on the task provided

    return {
        "primary": {
            "provider": Config.PRIMARY_PROVIDER,
            "model": Config.PRIMARY_MODEL
        },

        "fallback": {
            "provider": Config.FALLBACK_PROVIDER,
            "model": Config.FALLBACK_MODEL
        }
    }
