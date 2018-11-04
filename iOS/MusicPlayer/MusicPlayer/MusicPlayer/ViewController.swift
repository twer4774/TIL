//
//  ViewController.swift
//  MusicPlayer
//
//  Created by WonIk on 2018. 11. 4..
//  Copyright © 2018년 Walter. All rights reserved.
//

import UIKit
import AVFoundation
import MediaPlayer

class ViewController: UIViewController{

    var audioPlayer: AVAudioPlayer!
    var audioFile: URL! //재생할 오디오의 파일명
    let MAX_VOLUME: Float = 10.0
    var progressTimer: Timer! //프로그레스 타이머 변수
    
    let timePlayerSelector:Selector = #selector(ViewController.updatePlayTime) //재생 타이머
    
    @IBOutlet var prMusic: UIProgressView!
    @IBOutlet var lbCurrent: UILabel!
    @IBOutlet var lbEnd: UILabel!
    
    @IBOutlet var btnPlay: UIButton!
    @IBOutlet var btnPause: UIButton!
    @IBOutlet var btnStop: UIButton!
    
    @IBOutlet var slVolume: UISlider!
    
    //MPMedia
    
    @IBOutlet var lbMusicTitle: UILabel!
    @IBOutlet var lbMusicURL: UILabel!
    
    let mediaPicekr = MPMediaPickerController(mediaTypes: .music)
    var mediaItem: MPMediaItem?
    var mediaLabel: String!
    var mediaURL: URL?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
       
    }

    
    override func viewWillAppear(_ animated: Bool) {
        selectAudioFile()
        initPlay()
    }
    
    func initPlay(){
        do {
            audioPlayer = try AVAudioPlayer(contentsOf: audioFile)
        } catch let error as NSError{
            print("Error-initPlay: \(error)")
        }
        
        slVolume.maximumValue = MAX_VOLUME //최대 볼륨을 10.0으로 초기화
        slVolume.value = 1.0 //슬라이더 볼륨은 1.0으로 초기화
        prMusic.progress = 0 //프로그레스 진행을 0으로 초기화
        
        audioPlayer.delegate = self
        audioPlayer.prepareToPlay()
        audioPlayer.volume = slVolume.value
        
        lbEnd.text = convertNSTimeInterval2String(audioPlayer.duration) //초단위 실수값 변경
        lbCurrent.text = convertNSTimeInterval2String(0)
        
        setPlayButtons(true, pause: false, stop: false)
    }

    //초단위로 바꿔주기
    func convertNSTimeInterval2String(_ time: TimeInterval) -> String{
        let min = Int(time/60)
        let sec = Int(time.truncatingRemainder(dividingBy: 60))
        let strTime = String(format: "%02d:%02d", min, sec)
        return strTime
    }
    
    //타이머의 시간을 레이블과 프로그레스 뷰에 표현
    @objc func updatePlayTime(){
        lbCurrent.text = convertNSTimeInterval2String(audioPlayer.currentTime)
        prMusic.progress = Float(audioPlayer.currentTime/audioPlayer.duration)
    }
    
    @IBAction func btnPlay(_ sender: Any) {
        audioPlayer.play()
        setPlayButtons(false, pause: true, stop: true)
        progressTimer = Timer.scheduledTimer(timeInterval: 0.1, target: self, selector: timePlayerSelector, userInfo: nil, repeats: true)
    }
    @IBAction func btnPause(_ sender: Any) {
        audioPlayer.pause()
        setPlayButtons(true, pause: false, stop: true)
    }
    @IBAction func btnStop(_ sender: Any) {
        audioPlayer.stop()
        setPlayButtons(true, pause: true, stop: false)
        audioPlayer.currentTime = 0
        lbCurrent.text = convertNSTimeInterval2String(0)
        progressTimer.invalidate() //타이머 무효화
    }
    @IBAction func changeVolume(_ sender: Any) {
        audioPlayer.volume = slVolume.value
    }
    
    func setPlayButtons(_ play: Bool, pause: Bool, stop: Bool){
        btnPlay.isEnabled = play
        btnPause.isEnabled = pause
        btnStop.isEnabled = stop
    }
    
    func selectAudioFile(){
        if mediaURL == nil{
         audioFile = Bundle.main.url(forResource: "Sicilian_Breeze", withExtension: "mp3")
        } else {
            audioFile = mediaURL
        }
    }
    
    //MPMedia
    @IBAction func btnMediaLibrary(_ sender: Any) {
        mediaPicekr.delegate = self
        mediaPicekr.allowsPickingMultipleItems = false
        mediaPicekr.prompt = "노래선택"
        present(mediaPicekr, animated: true)
    }
    

}

extension ViewController: AVAudioPlayerDelegate{
    //오디오 재생이 끝나면 맨 처음 상태로 돌아가는 함수 추가
    func audioPlayerDidFinishPlaying(_ player: AVAudioPlayer, successfully flag: Bool) {
        progressTimer.invalidate()
        setPlayButtons(true, pause: false, stop: false)
    }
}
extension ViewController: MPMediaPickerControllerDelegate{
    func mediaPicker(_ mediaPicker: MPMediaPickerController, didPickMediaItems mediaItemCollection: MPMediaItemCollection) {

        mediaURL = mediaItemCollection.items[0].value(forProperty: MPMediaItemPropertyAssetURL) as! URL

        lbMusicTitle.text = mediaItemCollection.items[0].value(forProperty: MPMediaItemPropertyTitle) as! String
        

        dismiss(animated: true, completion: nil)
    }
    
    func mediaPickerDidCancel(_ mediaPicker: MPMediaPickerController) {
        self.dismiss(animated: true, completion: nil)
    }
}
