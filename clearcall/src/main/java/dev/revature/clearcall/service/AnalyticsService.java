package dev.revature.clearcall.service;

import dev.revature.clearcall.model.CallByDateKey;
import dev.revature.clearcall.repository.CallByAgentRepository;
import dev.revature.clearcall.repository.CallByCategoryRepository;
import dev.revature.clearcall.repository.CallByDateRepository;
import org.springframework.stereotype.Service;

@Service
public class AnalyticsService {
    private final CallByAgentRepository callByAgentRepository;
    private final CallByDateRepository callByDateRepository;
    private final CallByCategoryRepository callByCategoryRepository;

    public AnalyticsService(CallByAgentRepository callByAgentRepository, CallByDateRepository callByDateRepository, CallByCategoryRepository callByCategoryRepository)
    {
        this.callByAgentRepository = callByAgentRepository;
        this.callByDateRepository = callByDateRepository;
        this.callByCategoryRepository = callByCategoryRepository;
    }


}
