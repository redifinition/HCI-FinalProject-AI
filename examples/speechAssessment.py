import speechmetrics as sm
import pprint
from audoai.noise_removal import NoiseRemovalClient
noise_removal = NoiseRemovalClient(api_key='c70f68814902e8705aa9d16ac84e91bf')
window = 15

# 使用单个方法进行语音质量评价
# 可供选择的方法：
# absolute_relative = "absolute",method = 'mosnet'
# absolute_relative = "absolute",method = 'srmr'
# absolute_relative = "relative",method = 'bsseval'
# absolute_relative = "relative",method = 'pesq'
# absolute_relative = "relative",method = 'sisdr'
# absolute_relative = "relative",method = 'stoi'
def singleSpeechAssessment(wav_url,absolute_relative="relative",method="pesq"):
    metrics = sm.load(absolute_relative + '.' + method,window)
    tests = wav_url

    # 侵入式
    if absolute_relative == 'relative':
        # 根据语音增强接口生成降噪音频即参照的音频
        # 由于本api收费，在debug时请注释掉下面两行代码
        #reference_result = noise_removal.process(wav_url)
        #reference_result.save('data/clean_audio.wav')
        reference = 'data/clean_audio.wav'
        scores = metrics(reference,tests)

    # 非侵入式
    else:

        scores = metrics(tests)
    pprint.pprint(scores)
    return scores

singleSpeechAssessment('data/m2_script1_ipad_confroom1.wav','absolute','mosnet')
singleSpeechAssessment('data/m2_script1_clean.wav','absolute','mosnet')
singleSpeechAssessment('data/m2_script1_produced.wav','absolute','mosnet')