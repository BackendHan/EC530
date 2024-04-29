package com.itheima.consumer.listener;

import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
public class MQListener {

    @RabbitListener(queues = "topic.queue1")
    public void listenTopicQueue(String msg) throws InterruptedException {
        System.out.println("1 implement：" + msg);
    }

    @RabbitListener(queues = "topic.queue2")
    public void listenTopicQueue1(String msg) throws InterruptedException {
        System.out.println("2 implement：" +msg);
    }
}
