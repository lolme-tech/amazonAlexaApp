from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

sb = SkillBuilder()

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "ようこそ、アレクサスキルキットへ。こんにちは、と言ってみてください。"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("ハローワールド", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response