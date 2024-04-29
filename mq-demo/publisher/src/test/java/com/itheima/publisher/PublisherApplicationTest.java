package com.itheima.publisher;

import org.junit.jupiter.api.Test;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class PublisherApplicationTest {

    @Autowired
    private RabbitTemplate rabbitTemplate;

    @Test
    public void testPublish(){
        String queueName = "Simple.queue";
        String msg = "message from idea2!";
        rabbitTemplate.convertAndSend(queueName, msg);
    }

    @Test
    public void testPublish2(){
        String queueName = "Work.queue";
        for(int i = 1;i<=50;i++){
            String msg = "Work from idea!" + i;
            rabbitTemplate.convertAndSend(queueName, msg);
        }

    }

    @Test
    public void testTopicPublish(){
        String exchangeName = "hmall.topic";
        String msg = "message from usa";
        rabbitTemplate.convertAndSend(exchangeName,"usa.news", msg);
    }
}
