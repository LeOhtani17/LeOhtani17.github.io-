using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Video;


public class VideoChange : MonoBehaviour
{
	public ChangeVideo sphereScript;
	// インスペクター上で変更後の動画を指定
	public VideoClip NewClip;
    // インスペクター上でVideoPlayerを指定
	public VideoPlayer VideoPlayerComponent;
	private GameObject refObj;
    void Start() {
		refObj = GameObject.Find( "CubeR" );
	}

	void Update()
	{
        sphereScript = refObj.GetComponent<ChangeVideo>();
		if (sphereScript.vchange==1)
		{
			VideoPlayerComponent.clip = NewClip;
		}
	}
}
