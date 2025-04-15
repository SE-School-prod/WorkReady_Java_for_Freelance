"""
@file guild_id_dict.py
@date 2023/07/31(月)
@author 藤原光基
@brief DiscordのID関連
@details 処理に必要な各種ID,トークン情報をまとめた辞書型変数。
@note 「NOTION_TOKEN」、「DISCORD_TOKEN」について、変更時は逐次用変更。
@bar 編集日時 編集者 編集内容
@bar 2023/07/31(月) 藤原光基 新規作成
@bar 2023/09/18(月) 藤原光基 使用用途に応じてキー変更
"""

import os

settings_dict = {
    "DEBUG_FLG": False,
    "TOKEN": {
        "NOTION":
        'secret_013tQKTmEmdOOWcBgcPBTKNN3wAOzgQhTSkN2t63M2U',  # Notionのトークン
    },
    "GUILD_ID": {
        "GUILD": 1229973127270891540,  # DiscordのWorkReadyチャットグループID
        # "BOT": 1234011911826182218,  # 「DiscortionJava」BOTのメッセージID
        "BOT": 1335433826071216138,  # 「DiscortionJava2」BOTのメッセージID
        "CHANNEL_ID_DAILY_REPORT": 1229973127304581149,  # daily report
        "CHANNEL_ID_BOT_TRAIN": 1236765890691989597,  # bot_train
        # "CHANNEL_ID_DOC_COMPLETE": 1161660408457867345,  # Wiki読了報告
        "CHANNEL_ID_INIT_SETTING": 1229973127304581147,  # 初期設定
        # "CHANNEL_ID_ENOROLLMENT_STATUS": 1165596826200711220, #ステータスチャンネル
        # "CHANNEL_ID_CONSULTATION_SERVICE": 1175594169478160464, #チケット制相談チャンネル
        # "CHANNEL_ID_CONFIRM_TICKET_NUM": 1188814216145141841, #チケットの枚数確認チャンネル
        # "CHANNEL_ID_CONSULTATION_REPORT": 1229973128512540690, #相談会対応チャンネル
    },
    "DIR": {
        "LOG": {
            "ERROR": "log_error",  # ログ保存先(エラー)
            "INFO": "log_info",  # ログ保存先(各種処理実行内容)
            "SYS": "log_sys",  # ログ保存先(全部)
        },
        "LOG_SAVE_DIR": "notion_api_logs",  # ログ保存先
        "RESERVATION_CYCLE_FILE":
        os.path.join("settings", "reservation_cycle.txt"),  # 相談会予約送信先
        "INSTRUCTOR_CYCLE_FILE":
        os.path.join("settings", "instructor_cycle.txt")  # 担当講師参照番号
    },
    "CURRICULUM_NUMBER_RANGE": {
        "PROGATE": {
            "MIN": 1,
            "MAX": 5
        },
        "UDEMY": {
            "MIN": 6,
            "MAX": 432
        },
        "PORTOFOLIO": {
            "MIN": 433,
            "MAX": 440
        }
    },
    "CURRICULUM_GUIDELINE_DATE_RANGE": {
        "PROGATE": {
            "DATE_NUM": 14,
            "DESCRIPTION": "2週間",
            "PERCENTAGE": 5
        },
        "UDEMY": {
            "DATE_NUM": 42,
            "DESCRIPTION": "6週間",
            "PERCENTAGE": 45
        },
        "PORTOFOLIO": {
            "DATE_NUM": 56,
            "DESCRIPTION": "8週間",
            "PERCENTAGE": 50
        }
    },
    "AITEMASU_URL": {
        "0": {
            "name": "武藤みさき",
            "url": 'https://app.aitemasu.me/u/kakuiphone7/workreadyclass',
            "VC_NAME": '相談会-武藤',
        },
        "1": {
            "name": "林田翼",
            "url": 'https://app.aitemasu.me/u/tsubasa1121998/workreadyclass',
            "VC_NAME": '相談会-林田',
        },
        "2": {
            "name": "藤原光基",
            "url": 'https://app.aitemasu.me/u/ra0039ip/workreadyclass',
            "VC_NAME": '相談会-藤原',
        },
        "3": {
            "name": "菊池幸大",
            "url": 'https://app.aitemasu.me/u/koudai/workreadyclass',
            "VC_NAME": '相談会-菊池',
        },
        "4": {
            "name": "新家魁人",
            "url": 'https://app.aitemasu.me/u/kniinominodo/irupcurriculum',
            "VC_NAME": '相談会-新家',
        },
    },
    "SENDING": {
        "3DAYS":{
            "TERM": "3日~4日",
            "MAIL": {
                "TITLE": "【必ずお読みください】最終進捗日から日数経過ご連絡",
                "CONTENT": "いつもお世話になっております。\n" +\
                           "WorkReady運営です。\n\n" +\
                           "最後に進捗をご報告いただきました日程から3日が経過いたしましため、\n" +\
                           "その後の進捗確認のためご連絡させていただきました。\n\n" +\
                           "入校より4ヵ月が経過しますと、月額料金の請求が開始されますのでご注意ください。\n\n" +\
                           "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                           "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                           "以上、よろしくお願いいたします。\n\n" +\
                           "--------------------------------------------------------------------------------------------------------\n" +\
                           "EastCloud株式会社\n" +\
                           "〒101-0063 東京都千代田区神田淡路町1-9-5 天翔御茶ノ水ビル505号室\n" +\
                           "Mail: workreadyschool@gmail.com"
            },
            "DM": "いつもお世話になっております。\n" +\
                  "WorkReady運営です。\n\n" +\
                  "ここ数日間の進捗が確認できませんが、いかがですか？\n\n" +\
                  "入校より4ヵ月が経過しますと、月額料金の請求が開始されますのでご注意ください。\n\n" +\
                  "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                  "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                  "以上、よろしくお願いいたします。"
        },
        "1WEEK":{
            "TERM": "1週間",
            "MAIL": {
                "TITLE": "【必ずお読みください】最終進捗日から日数経過ご連絡",
                "CONTENT": "いつもお世話になっております。\n" +\
                           "WorkReady運営です。\n\n" +\
                           "最後に進捗をご報告いただきました日程から1週間が経過いたしましため、\n" +\
                           "その後の進捗確認のためご連絡させていただきました。\n\n" +\
                           "入校より4ヵ月が経過しますと、月額料金の請求が開始されますのでご注意ください。\n\n" +\
                           "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                           "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                           "以上、よろしくお願いいたします。\n\n" +\
                           "--------------------------------------------------------------------------------------------------------\n" +\
                           "EastCloud株式会社\n" +\
                           "〒101-0063 東京都千代田区神田淡路町1-9-5 天翔御茶ノ水ビル505号室\n" +\
                           "Mail: workreadyschool@gmail.com"
            },
            "DM": "いつもお世話になっております。\n" +\
                  "WorkReady運営です。\n\n" +\
                  "ここ1週間の進捗が確認できませんが、いかがですか？\n\n" +\
                  "入校より4ヵ月が経過しますと、月額料金の請求が開始されますのでご注意ください。\n\n" +\
                  "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                  "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                  "以上、よろしくお願いいたします。"
        },
        "10DAYS":{
            "TERM": "1o日~11日",
            "MAIL": {
                "TITLE": "【必ずお読みください】最終進捗日から日数経過ご連絡",
                "CONTENT": "いつもお世話になっております。\n" +\
                           "WorkReady運営です。\n\n" +\
                           "最後に進捗をご報告いただきました日程から10日が経過いたしましため、\n" +\
                           "その後の進捗確認のためご連絡させていただきました。\n\n" +\
                           "入校より4ヵ月が経過しますと、月額料金の請求が開始されますのでご注意ください。\n\n" +\
                           "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                           "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                           "以上、よろしくお願いいたします。\n\n" +\
                           "--------------------------------------------------------------------------------------------------------\n" +\
                           "EastCloud株式会社\n" +\
                           "〒101-0063 東京都千代田区神田淡路町1-9-5 天翔御茶ノ水ビル505号室\n" +\
                           "Mail: workreadyschool@gmail.com"
            },
            "DM": "いつもお世話になっております。\n" +\
                  "WorkReady運営です。\n\n" +\
                  "ここ10日間の進捗が確認できませんが、いかがですか？\n\n" +\
                  "入校より4ヵ月が経過しますと、月額料金の請求が開始されますのでご注意ください。\n\n" +\
                  "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                  "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                  "以上、よろしくお願いいたします。"
        },
        "2WEEKS":{
            "TERM": "2週間",
            "MAIL": {
                "TITLE": "【必ずお読みください】最終進捗日から日数経過ご連絡",
                "CONTENT": "いつもお世話になっております。\n" +\
                           "WorkReady運営です。\n\n" +\
                           "最後に進捗をご報告いただきました日程から2週間が経過いたしましため、\n" +\
                           "その後の進捗確認のためご連絡させていただきました。\n\n" +\
                           "入校より4ヵ月が経過しますと、月額料金の請求が開始されますのでご注意ください。\n\n" +\
                           "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                           "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                           "以上、よろしくお願いいたします。\n\n" +\
                           "--------------------------------------------------------------------------------------------------------\n" +\
                           "EastCloud株式会社\n" +\
                           "〒101-0063 東京都千代田区神田淡路町1-9-5 天翔御茶ノ水ビル505号室\n" +\
                           "Mail: workreadyschool@gmail.com"
            },
            "DM": "いつもお世話になっております。\n" +\
                  "WorkReady運営です。\n\n" +\
                  "ここ2週間の進捗が確認できませんが、いかがですか？\n\n" +\
                  "入校より4ヵ月が経過しますと、月額料金の請求が開始されますのでご注意ください。\n\n" +\
                  "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                  "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                  "以上、よろしくお願いいたします。"
        },
        "1MONTH": {
            "TERM": "1ヵ月",
            "MAIL": {
                "TITLE": "【必ずお読みください】入校から1ヵ月経過のご連絡",
                "CONTENT": "いつもお世話になっております。\n" +\
                           "WorkReady運営です。\n\n" +\
                           "入校より1ヵ月が経過いたしましたことをご報告いたします。\n" +\
                           "入校より4ヵ月が経過いたしますと、月額料金の請求が開始されますのでご注意ください。\n\n" +\
                           "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                           "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                           "以上、よろしくお願いいたします。\n\n" +\
                           "--------------------------------------------------------------------------------------------------------\n" +\
                           "EastCloud株式会社\n" +\
                           "〒101-0063 東京都千代田区神田淡路町1-9-5 天翔御茶ノ水ビル505号室\n" +\
                           "Mail: workreadyschool@gmail.com"
            },
            "DM": "いつもお世話になっております。\n" +\
                  "WorkReady運営です。\n\n" +\
                  "入校より1ヵ月が経過いたしましたことをご報告いたします。\n" +\
                  "入校より4ヵ月が経過いたしますと、月額料金の請求が開始されますのでご注意ください。\n\n"+\
                  "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                  "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                  "以上、よろしくお願いいたします。"
        },
        "2MONTH": {
            "TERM": "2ヵ月",
            "MAIL": {
                "TITLE": "【必ずお読みください】入校から2ヵ月経過のご連絡",
                "CONTENT": "いつもお世話になっております。\n" +\
                           "WorkReady運営です。\n\n" +\
                           "入校より2ヵ月が経過いたしましたことをご報告いたします。\n" +\
                           "入校より4ヵ月が経過いたしますと、月額利用料金の請求が開始されますのでご注意ください。\n\n"+\
                           "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                           "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                           "以上、よろしくお願いいたします。\n\n" +\
                           "--------------------------------------------------------------------------------------------------------\n" +\
                           "EastCloud株式会社\n" +\
                           "〒101-0063 東京都千代田区神田淡路町1-9-5 天翔御茶ノ水ビル505号室\n" +\
                           "Mail: workreadyschool@gmail.com"
            },
            "DM": "いつもお世話になっております。\n" +\
                  "WorkReady運営です。\n\n" +\
                  "入校より2ヵ月が経過いたしましたことをご報告いたします。\n" +\
                  "入校より4ヵ月が経過いたしますと、月額利用料金の請求が開始されますのでご注意ください。\n\n"+\
                  "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                  "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                  "以上、よろしくお願いいたします。"
        },
        "3MONTH": {
            "TERM": "3ヵ月",
            "MAIL": {
                "TITLE": "【必ずお読みください】入校から3ヵ月経過のご連絡",
                "CONTENT": "いつもお世話になっております。\n" +\
                           "WorkReady運営です。\n\n" +\
                           "入校より3ヵ月が経過いたしましたことをご報告いたします。\n" +\
                           "入校より4ヵ月が経過いたしますと、月額利用料金の請求が開始されますのでご注意ください。\n\n"+\
                           "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                           "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                           "以上、よろしくお願いいたします。\n\n" +\
                           "--------------------------------------------------------------------------------------------------------\n" +\
                           "EastCloud株式会社\n" +\
                           "〒101-0063 東京都千代田区神田淡路町1-9-5 天翔御茶ノ水ビル505号室\n" +\
                           "Mail: workreadyschool@gmail.com"
            },
            "DM": "いつもお世話になっております。\n" +\
                  "WorkReady運営です。\n\n" +\
                  "入校より3ヵ月が経過いたしましたことをご報告いたします。\n" +\
                  "入校より4ヵ月が経過いたしますと、月額料金の請求が開始されますのでご注意ください。\n\n"+\
                  "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                  "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                  "以上、よろしくお願いいたします。"
        },
        "4MONTH": {
            "TERM": "4ヵ月",
            "MAIL": {
                "TITLE": "【必ずお読みください】月額料金請求開始ご連絡",
                "CONTENT": "いつもお世話になっております。\n" +\
                           "WorkReady運営です。\n\n" +\
                           "入校より4ヵ月が経過いたしましたことをご報告いたします。\n" +\
                           "それに伴い、月額料金の請求が開始いたしますため、ご認識のほどよろしくお願いいたします。\n\n"+\
                           "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                           "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                           "以上、よろしくお願いいたします。\n\n" +\
                           "--------------------------------------------------------------------------------------------------------\n" +\
                           "EastCloud株式会社\n" +\
                           "〒101-0063 東京都千代田区神田淡路町1-9-5 天翔御茶ノ水ビル505号室\n" +\
                           "Mail: workreadyschool@gmail.com"
            },
            "DM": "いつもお世話になっております。\n" +\
                  "WorkReady運営です。\n\n" +\
                  "入校より4ヵ月が経過いたしましたことをご報告いたします。\n" +\
                  "それに伴い、月額料金の請求が開始いたしますため、ご認識のほどよろしくお願いいたします。\n\n"+\
                  "不明点により進捗が進まない場合は、予約チケットを用いて相談会をご利用ください。\n" +\
                  "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n" +\
                  "以上、よろしくお願いいたします。"
        },
        # "NOTIFY": {
        #     "TERM": "3日~4日",
        #     "MAIL": {
        #         "TITLE": "【必ずお読みください】最終進捗日から日数経過ご連絡",
        #         "CONTENT": "いつもお世話になっております。\n"+\
        #                    "WorkReady運営です。\n\n"+\
        #                    "最後に進捗をご報告いただきました日程から3日が経過いたしましため、\n"+\
        #                    "その後の進捗確認のためご連絡させていただきました。\n\n"+\
        #                    "不明点により進捗が進まない場合は、毎週２回開催しております相談会をご利用ください。\n"+\
        #                    "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n"+\
        #                    "以上、よろしくお願いいたします。\n\n"+\
        #                    "--------------------------------------------------------------------------------------------------------\n"+\
        #                    "株式会社iConnect\n"+\
        #                    "〒108-0075 東京都港区港南4-6-3-3401\n"+\
        #                    "Mail: workreadyschool@gmail.com"
        #     },
        #     "DM": "いつもお世話になっております。\n"+\
        #           "WorkReady運営です。\n\n"+\
        #           "ここ数日間の進捗が確認できませんが、いかがですか？\n\n"+\
        #           "不明点により進捗が進まない場合は、毎週２回開催しております相談会をご利用ください。\n"+\
        #           "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n"+\
        #           "以上、よろしくお願いいたします。"
        # },
        # "WARNING": {
        #     "TERM": "1週間程度",
        #     "MAIL": {
        #         "TITLE": "【必ずお読みください】最終進捗日から日数経過ご連絡【再送】",
        #         "CONTENT": "いつもお世話になっております。\n"+\
        #                    "WorkReady運営です。\n\n"+\
        #                    "最後に進捗報告を頂きました日程から1週間が経過いたしましため、\n"+\
        #                    "その後の進捗確認のためご連絡させていただきました。\n\n"+\
        #                    "14日間進捗が確認できない場合\n"+\
        #                    "契約に基づき当コミュニティより除名させていただくとともに\n"+\
        #                    "受講料132,000円(税込)をご請求させていただきます。\n\n"+\
        #                    # "このまま進捗のご報告がない場合、下記日程にて受講料をご請求させていただきます。\n"+\
        #                    # "{}\n\n"+\
        #                    "不明点により進捗が進まない場合は、相談チャンネルや週次で実施しております相談会をご利用ください。\n"+\
        #                    "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n"+\
        #                    "以上、よろしくお願いいたします。\n\n"+\
        #                    "--------------------------------------------------------------------------------------------------------\n"+\
        #                    "株式会社iConnect\n"+\
        #                    "〒108-0075 東京都港区港南4-6-3-3401\n"+\
        #                    "Mail: workreadyschool@gmail.com"
        #     },
        #     "DM": "いつもお世話になっております。\n"+\
        #           "WorkReady運営です。\n\n"+\
        #           "ここ1週間の進捗が確認できません。\n"+\
        #           "14日間進捗が確認できない場合\n"+\
        #           "契約に基づき当コミュニティより除名させていただくとともに\n"+\
        #           "受講料132,000円(税込)をご請求させていただきます。\n\n"+\
        #           "不明点により進捗が進まない場合は、相談チャンネルや週次で実施しております相談会をご利用ください。\n"+\
        #           "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n"+\
        #           "以上、よろしくお願いいたします。"
        # },
        # "ULTIMATUM": {
        #     "TERM": "12日~13日",
        #     "MAIL": {
        #         "TITLE": "【必ずお読みください】最終進捗日から日数経過ご連絡【最終通告】",
        #         "CONTENT": "いつもお世話になっております。\n"+\
        #                    "WorkReady運営です。\n\n"+\
        #                    "受講料ご請求までの日程が残り3日となりましたため、\n"+\
        #                    "現状の進捗をご入力いただきたくご連絡させていただきました。\n\n"+\
        #                    "14日間進捗が確認できない場合\n"+\
        #                    "契約に基づき当コミュニティより除名させていただくとともに\n"+\
        #                    "受講料132,000円(税込)をご請求させていただきます。\n\n"+\
        #                    # "このまま進捗のご報告がない場合、下記日程にて受講料をご請求させていただきます。\n"+\
        #                    # "{}\n\n"+\
        #                    "不明点により進捗が進まない場合は、相談チャンネルや週次で実施しております相談会をご利用ください。\n"+\
        #                    "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n"+\
        #                    "以上、よろしくお願いいたします。\n\n"+\
        #                    "--------------------------------------------------------------------------------------------------------\n"+\
        #                    "株式会社iConnect\n"+\
        #                    "〒108-0075 東京都港区港南4-6-3-3401\n"+\
        #                    "Mail: workreadyschool@gmail.com"
        #     }, 
        #     "DM": "いつもお世話になっております。\n"+\
        #           "WorkReady運営です。\n\n"+\
        #           "規約違反規定日数まで残り3日となりました。\n"+\
        #           "14日間進捗が確認できない場合\n"+\
        #           "契約に基づき当コミュニティより除名させていただくとともに\n"+\
        #           "受講料132,000円(税込)をご請求させていただきます。\n\n"+\
        #           "不明点により進捗が進まない場合は、相談チャンネルや週次で実施しております相談会をご利用ください。\n"+\
        #           "また、やむを得ない事情により進捗を勧められない場合は担当の代理店様にご連絡ください。\n\n"+\
        #           "以上、よろしくお願いいたします。"
        # },
        # "BAN": {
        #     "TERM": "15日以上",
        #     "MAIL": {
        #         "TITLE": "【必ずお読みください】退会措置とIT技術学習費用のお支払いについて",
        #         "CONTENT": "いつもお世話になっております。\n"+\
        #                    "Work Ready運営です。\n\n"+\
        #                    "この度、貴殿が当スクールのStarterプラン個別利用規約に違反していることが判明したため退会措置を採らせてていただきました。\n"+\
        #                    "つきましては、Starterプラン個別利用規約に基づき、入会金を請求いたします。\n\n"+\
        #                    "下記URLより請求金額をご確認の上、お支払いをお願いいたします。\n"+\
        #                    "請求期限は[当月末]とさせていただきます。\n"+\
        #                    "https://buy.stripe.com/14kcPg8qlcgo0Rq9AF\n\n"+\
        #                    "お支払いいただけない場合、支払督促や訴訟などの法的手続を採る場合がございます。\n\n"+\
        #                    "何卒、ご理解とご協力のほどよろしくお願い申し上げます。\n"+\
        #                    "--------------------------------------------------------------------------------------------------------\n"+\
        #                    "株式会社iConnect\n"+\
        #                    "〒108-0075 東京都港区港南4-6-3-3401\n"+\
        #                    "Mail: workreadyschool@gmail.com"
        #     },
        #     "DM": ""
        # },
    }
}
