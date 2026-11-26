# Rebuild notes: purple "미확인 보험내역" motion v6

Target file: `meritz_bojang_unconfirmed_motion_9x16_v6.mp4`. It was 1080×1920, 17.64 s, 30 fps, H.264 + AAC. It was rendered on 2026-10-27 at 07:18–07:19Z from `scratchpad/unkv3/site/`.

All of this comes from the server transcript of session_013e8rDmejoULvKZjUJrMpP5. Every timestamp below is UTC.

## 1. HTML (`site/index.html`): fully recovered
- **Base:** the full `Write` of `unk/site/index.html` at 2026-10-22 09:21:55. That is v1, square 1080×1080.
- **Patches:** applied in the order below. Every `assert s.count(a)==1` passed during the replay (`history/replay_patches.py`).

| # | Time | Script | Folder | Change |
|---|---|---|---|---|
| 1 | 10-22 10:47:39 | `p1_1022_1047.sh` | unkv/site | Switch to 9:16; red grunge "보장분석 무료" stamp; 3D objects (bell, phone_n, docs, mag, alert, holo); sparks |
| 2 | 10-22 10:48:05 | `p2_1022_1048.sh` | unkv/site | Grunge matrix tweak; scan/res panels zoom 1.25 → **v2** |
| 3 | 10-27 03:42:53 | `p3_1027_0342.sh` | unkv3/site | Cards replaced by 3 push-notification banners; `free.png` stamp; Meri `m_doc`/`m_wink` |
| 4 | 10-27 03:43:17 | `p4_1027_0343.sh` (sed) | unkv3/site | `html{background:#5B2B70}` → **v3** (v4 changed only the image, not the HTML) |
| 5 | 10-27 07:11:09 | `p5_1027_0711a.sh` | unkv3/site | Timeline −0.76 s; bigger "1분이면 끝!" title (150px), bigger FREE, m_wink and holo; sparks re-centred |
| 6 | 10-27 07:11:22 | `p6_1027_0711b.sh` (sed) | unkv3/site | Badge, bell, phone and typing dots come in earlier → **v5** |
| 7 | 10-27 07:18:29 | `p7_1027_0718.sh` | unkv3/site | Timeline rebuilt with D=0.36 and N[0]=0.6; T0 title at 0.55; badge pops at 0.15–0.45 s → **v6** |

**Check against the transcript:** the replayed file gives exactly the line numbers the transcript's own `grep -n` printed at 07:10:34 and 07:11:22: lines 14, 20, 35, 53, 59, 66, 85, 92, 123, 125, 90, 97, 118, 119.

Intermediate versions are in `history/` (v1, v2, v3/v4, v5).

The page needs:
- Pretendard **Medium/SemiBold/Bold/ExtraBold** `.woff2` in `site/`, under the same file names, e.g. `Pretendard-Bold.woff2`.
- A colour-emoji font on the render machine, for 🔔 and 👆.

## 2. Timeline (v6)
```
const N=[0.6,2.79,5.69,9.94,12.59]            // narration start times n1..n5
const SC=[0,2.64,5.54,9.79,12.44,15.24]        // scene starts
const END=15.24; window.DURATION=17.64         // end card from 15.24 to 17.64
```
| Scene | Time (s) | On screen |
|---|---|---|
| S#1 | 0–2.64 | "미확인 / 보험내역이 있습니다", typing dots, profile ring, red 1 badge (pops at 0.15–0.45), bell, phone |
| S#2 | 2.64–5.54 | "잊고 있던 내 보험, 몇 개인지 아세요?"; 3 notification banners (실손 2014 / 암 2017 / 운전자 2019) at +0.2/+1.2/+1.6; docs |
| S#3 | 5.54–9.79 | "흩어진 보험을 한 번에 조회!"; scan panel; magnifier object; Meri `m_doc` |
| S#4 | 9.79–12.44 | "부족한 보장까지 바로 확인"; result panel with 보험점수 11점 gauge and 암/뇌혈관/심장 부족 tags; alert icon at +1.2 with beep |
| S#5 | 12.44–15.24 | "1분이면 끝!"; FREE stamp slams at +0.15 (with shake and sparks); Meri `m_wink` (fist); holo orb; finger taps the bottom bar |
| S#6 | 15.24–17.64 | `endcard.png` |

Fixed elements: the `준법감시인 심의필 제OOOO호 (2026.OO.OO~2027.OO.OO)` placeholder and the bottom bar "앱에서 1분 확인하기 ›".

## 3. Narration
- **Voice:** Higgsfield `elevenlabs_v4`, preset voice **Ainsley** `731b4ffe-e95e-59f4-8c00-81608936091f`.

| File | Text | Generated | Settings |
|---|---|---|---|
| n1.wav | 미확인 보험내역이 있습니다. | 10-27 07:10:44 (takes a and b; **b** was used, 1.790 s after processing) | `--stability 0.7` |
| n2.wav | 잊고 있던 내 보험, 몇 개인지 아세요? | 10-22 09:20:54 | default stability |
| n3.wav | 메리츠화재 보장분석으로, 흩어진 보험을 한 번에 조회하고, | 10-22 09:20:54 | default |
| n4.wav | 부족한 보장까지 바로 확인하세요. | 10-22 09:20:54 | default |
| n5.wav | 무료로, 일 분이면 끝! | 10-22 09:20:54 | default |

The v1–v4 n1 ("띵동! 미확인 보험내역이 있습니다!") was replaced in v5.

Generation command (from `history/vo_v1.sh`):
```
higgsfield generate create elevenlabs_v4 --dialogue '[{"text":"<TEXT>","voice_id":"731b4ffe-e95e-59f4-8c00-81608936091f","voice_type":"preset"}]' [--stability 0.7] --wait --wait-timeout 10m
```
Post-processing:
```
# n2..n5 (10-22)
ffmpeg -i vo/nX.mp3 -af "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=stop_periods=-1:stop_duration=0.15:stop_threshold=-38dB:stop_silence=0.1,atempo=1.15" -ar 48000 site/nX.wav
# n1 (10-27)
ffmpeg -i vo/n1b.mp3 -af "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,atempo=1.15" -ar 48000 site/n1.wav
```
Durations after processing (use these to check regenerated takes):
- 10-22 originals: n2 2.336 s, n3 3.912 s, n4 2.245 s, n5 1.472 s.
- n1 1.790 s.

## 4. Locally made assets (code)
**beep.wav**, the 11점 warning beep. Already regenerated into `site/`.
```
ffmpeg -y -f lavfi -i "aevalsrc='0.45*sin(2*PI*1550*t)*(lt(t,0.17)+gt(t,0.24)*lt(t,0.62))*min(1,mod(t,10)*200)':s=48000:d=0.7" -af "afade=t=out:st=0.55:d=0.07" beep.wav
```

**dingdong.wav**, the opening doorbell. Already regenerated into `site/`.
```
ffmpeg -y -f lavfi -i "aevalsrc='0.5*sin(2*PI*1318*t)*exp(-4*t)*lt(t,0.42)+0.5*sin(2*PI*1046*(t-0.38))*exp(-3*(t-0.38))*gt(t,0.38)+0.15*sin(2*PI*2636*t)*exp(-8*t)':s=48000:d=1.4" -af "afade=t=in:d=0.005,afade=t=out:st=1.1:d=0.3" dingdong.wav
```

**m_wink.png** (the fist Meri) is `sg/gen/m_wink_fist.png`, made on 10-27 between 06:37 and 06:38. It needs `gen/m_wink.png` and `gen/m_wink2.png` (see section 5).
```
higgsfield generate create gpt_image_2_5 --prompt "Edit this image: keep the exact same character, smartphone, wink expression, pose and transparent background. Only change the hand doing a thumbs up into a simple relaxed closed fist held at chest height, no thumbs up gesture. No text." --image-references gen/m_wink.png --aspect_ratio 1:1 --resolution 1k --quality high --background transparent   # -> gen/m_wink2.png
python3 - <<'EOF'
from PIL import Image,ImageDraw,ImageFilter
a=Image.open('gen/m_wink.png').convert('RGBA');b=Image.open('gen/m_wink2.png').convert('RGBA')
m=Image.new('L',a.size,0);ImageDraw.Draw(m).rectangle((240,500,445,770),fill=255);m=m.filter(ImageFilter.GaussianBlur(10))
Image.composite(b,a,m).save('gen/m_wink_fist.png')
EOF
```

## 5. Generated or copied assets I could NOT recover
The Higgsfield result URLs were never printed in the transcript: every call sent its output to a `*.txt` file and passed the URL straight to curl. Higgsfield URLs follow the pattern `https://d8j0ntlcm91z4.cloudfront.net/user_<id>/hf_YYYYMMDD_HHMMSS_<jobid>.<ext>`. Old URLs from 10-08 still download, so finding the job IDs in the account's job history should be enough. The history API supports a `cursor`, but `higgsfield generate list` only shows the newest 100 jobs.

| File in site/ | Origin | Time window (UTC) | Prompt / notes |
|---|---|---|---|
| n1.wav | elevenlabs_v4 (see section 3) | 10-27 07:10:44–07:10:51 | 2 takes; pick the one that gives 1.790 s after processing |
| n2–n5.wav | elevenlabs_v4 | 10-22 09:20:54–09:21:04 | texts in section 3 |
| bell.png | gpt_image_2_5, 1:1, 1k, high, transparent | 10-22 10:46:29–10:47:39 | "A shiny golden notification bell ringing with small motion lines and a red dot badge, cute glossy 3D icon, soft clay-plastic render, single object centered, isolated on transparent background, no text, no letters" |
| phone_n.png | same | same | "A white smartphone with a bright red notification bubble popping out of the screen and small sparkles, " + same suffix |
| alert.png | same | same | "A red rounded triangle warning sign with a white exclamation mark, " + same suffix |
| m_doc.png | gpt_image_2_5, `--image-references ../mm/m_front.png`, 1:1, 1k, high, transparent | 10-22 10:39–10:44 | "Keep this exact character design (orange petal hair, red shirt with M logo). The character wears a cute light blue surgical cap and holds up a clipboard with a big red check mark, proud confident smile, full body, isolated on transparent background, no text" |
| m_wink.png base (gen/m_wink.png) | same | 10-22 10:39–10:44 | "Keep this exact character design (orange petal hair, red shirt with M logo). The character gives a thumbs up with one hand and holds a smartphone in the other, winking, full body, isolated on transparent background, no text" |
| gen/m_wink2.png | gpt_image_2_5 edit (section 4) | 10-27 06:37:22–06:38:16 | then composited as in section 4 |
| mag.png, docs.png, holo.png | copied from `bm/site/` (first 보장분석 motion) | made before 10-22 | prompts are not in the range I scanned |
| free.png | copied from `h100/site/free.png` (100세 shorts) | before 10-27 | red FREE stamp image; prompt not in scanned range |
| endcard.png | copied from `end19/endcard_final.png` | before 10-22 | the white end card (S#6, "1분만에 보험 진단 받기 ›", as described for the video); I did not see its contents or how it was built in the scanned range |
| logo_white.png | copied from `mm/logo_white.png` | before 10-22 | white Meritz logo (header) |
| click3.wav, whoosh.wav | copied from `fvv/sfx/` | before 10-22 | described as "clear synthesized click3.wav"; code not in scanned range |
| bgm.m4a | copied from `bm/site/bgm.m4a` | before 10-22 | "지난 보장분석 모션 1차 버전 곡"; it is also mixed into `creatives/2026-11-05/emoji_bojang_motion/source_v3.mp4`, but only with narration on top |

The scanned range is 2026-10-22 09:12Z to 2026-11-05. Everything marked "before 10-22" was built earlier in the session.

## 6. Final mix (`mix5.wav`) and render
Run in `site/`, as in the v6 script (`history/p7_1027_0718.sh`).
```python
import subprocess
D=0.36
N=[0.6,3.15-D,6.05-D,10.3-D,12.95-D];SC=[0,3.0-D,5.9-D,10.15-D,12.8-D,15.6-D];END=15.6-D;TOT=18.0-D
ev=[(f'n{i+1}.wav',N[i],1.0) for i in range(5)]+[('dingdong.wav',0.03,0.55),('click3.wav',SC[1]+0.2,0.35),('click3.wav',SC[1]+1.2,0.35),('click3.wav',SC[1]+1.6,0.35)]+[('whoosh.wav',s-0.06,0.12) for s in SC[1:5]]+[('beep.wav',SC[3]+1.2,0.55),('click3.wav',SC[4]+0.31,0.8),('click3.wav',END-0.75,0.85)]
inp=[];fl=[];vo=[];fx=[]
for j,(f,t,v) in enumerate(ev):
    inp+=['-i',f];ms=int(t*1000);fl.append(f'[{j}]aformat=sample_rates=48000:channel_layouts=stereo,volume={v},adelay={ms}|{ms}[a{j}]');(vo if f[0]=='n' else fx).append(f'[a{j}]')
n=len(ev);inp+=['-i','bgm.m4a']
fl.append(''.join(vo)+f'amix=inputs={len(vo)}:normalize=0,apad,atrim=0:{TOT},asplit[v1][v2]')
fl.append(''.join(fx)+f'amix=inputs={len(fx)}:normalize=0,apad,atrim=0:{TOT}[fx]')
fl.append(f'[{n}]aformat=sample_rates=48000:channel_layouts=stereo,apad,atrim=0:{TOT},volume=0.45,afade=t=out:st={TOT-1.5}:d=1.5[bg]')
fl.append('[bg][v2]sidechaincompress=threshold=0.03:ratio=5:attack=20:release=300[bgd]')
fl.append('[bgd][v1][fx]amix=inputs=3:normalize=0:duration=first,apad,atrim=0:%s,loudnorm=I=-14:TP=-1.5[out]'%TOT)
subprocess.run(['ffmpeg','-y','-loglevel','error',*inp,'-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','mix5.wav'],check=True)
```
Render and mux, from the `unk_rebuild/` folder:
```
W=1080 H=1920 node render.cjs site frames fr
ffmpeg -y -loglevel error -framerate 30 -i fr/f%05d.jpg -i site/mix5.wav -af apad -c:v libx264 -pix_fmt yuv420p -crf 18 -c:a aac -b:a 192k -t 17.64 meritz_bojang_unconfirmed_motion_9x16_v6.mp4
```
`render.cjs` here is a **reconstruction** with the same interface (W/H/Q/TS env, stills/frames modes, f%05d.jpg at 30 fps, t<ts>.png). The original source is not in the transcript I scanned.

## 7. Reference
- `ref/original_purple_image_creative.webp`: the user's high-performing image creative. It was sent at 10-22 09:20:06 with "이 소재가 이미지 소재에서 되게 잘 되거든? 이걸 영상화해서…18초".
- Its real 심의필 was 제2025-광고-1007호 (2025.05.19~2026.05.18). The video keeps the OOOO placeholder.
