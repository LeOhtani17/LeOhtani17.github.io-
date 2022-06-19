using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Gravity : MonoBehaviour
{
    public GameObject gravity;
    private Vector3 lastPosition;

    void Start()
    {
        lastPosition = transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        gravity.transform.localPosition = Vector3.zero;
        gravity.transform.localRotation = Quaternion.identity;
        gravity.GetComponent<Rigidbody>().velocity = (transform.position - lastPosition) / Time.deltaTime;
        lastPosition = transform.position;
    }
}
