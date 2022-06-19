using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Photon.Pun;
 
public class Touch : MonoBehaviour
{
	public Spawner spawner;
	public ParticleSystem particle;
	// 音データの再生装置を格納する変数
	private AudioSource audio;
	public int clap=0;
	// 音データを格納する変数（Inspectorタブからも値を変更できるようにする）
	[SerializeField]
	private AudioClip sound;
	

	// Start is called before the first frame update
	void Start()
    {
		// ゲームスタート時にAudioSource（音再生装置）のコンポーネントを加える
		audio = gameObject.AddComponent<AudioSource>();
		//photonView    = GetComponent<PhotonView>();
	}

	void OnCollisionEnter(Collision collision)
	{
		// 衝突した相手にHandRタグが付いているとき
		if (collision.gameObject.tag == "HandR")
			{	
				clap=clap+1;
				if (clap==2){
					audio.PlayOneShot(sound);
					Instantiate(particle, new Vector3( 0.0f, 0.0f, 0.0f), Quaternion.identity);
            		//particle.Play();
					clap=1;
				}

				
			}
	}
	void Update(){
		if (spawner.count==1){
		particle.Stop();
		}
	}
}