using System.Collections;
using System.Collections.Generic;
using UnityEngine;   

public class SePlay : MonoBehaviour
{
    [SerializeField]   
    AudioClip[] audioClips;
    AudioSource audioSource;  
    // Start is called before the first frame update
    void Start()
    {
        audioSource = GetComponent<AudioSource>();
    }
    public void PlaySound(string seName)
    {
        switch (seName)
        {
            case "SE0":
                audioSource.PlayOneShot(audioClips[0]);
                break;
            case "SE1":
                audioSource.PlayOneShot(audioClips[1]);
                break;
            case "SE2":
                audioSource.PlayOneShot(audioClips[2]);
                break;
            case "SE3":
                audioSource.PlayOneShot(audioClips[3]);
                break;
            case "SE4":
                audioSource.PlayOneShot(audioClips[4]);
                break;
            case "SE5":
                audioSource.PlayOneShot(audioClips[5]);
                break;
            case "SE6":
                audioSource.PlayOneShot(audioClips[6]);
                break;
            case "SE7":
                audioSource.PlayOneShot(audioClips[7]);
                break;
            case "SE8":
                audioSource.PlayOneShot(audioClips[8]);
                break;
            case "SE9":
                audioSource.PlayOneShot(audioClips[9]);
                break;
        }
    }
}