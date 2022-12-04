###################################################
#処理要求が発声したときにハンドラが対応
###################################################

#スキルビルダーオブジェクト
from ask_sdk_core.skill_builder import SkillBuilder
#陸セストを処理して応答を返すリクエストハンドラー
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

#入力されたリクエスト処置とカスタム応答の生成
sb = SkillBuilder()

#受け取ったリクエストがLaunchRequestの時、can_handle関数の戻り値はTrue
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

#HelloWorldIntentという院展とリクエストを受け取ったときに呼び出されるハンドラを設定する
class HelloWorldIntentHandler(AbstractRequestHandler):
    #処理要求がIntentRequestの時かつインテント名がHelloWorldIntentの時Trueを返す
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("HelloWorldIntent")(handler_input)

    #「こんにちは」という応答生成
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "こんにちは"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("ハローワールド", speech_text)).set_should_end_session(
            True)
        return handler_input.response_builder.response

class HelpIntentHandler(AbstractRequestHandler):
    #処理要求がIntentRequestの時かつAMAZON.HelpIntentの時Trueを返す
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "こんにちは。と言ってみてください。"
        #.ask(speech_text)でユーザのマイクがオンになりユーザの応答待ち
        handler_input.response_builder.speak(speech_text).ask(speech_text).set_card(
            SimpleCard("ハローワールド", speech_text))
        return handler_input.response_builder.response

class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "さようなら"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("ハローワールド", speech_text)).set_should_end_session(True)
        return handler_input.response_builder.response