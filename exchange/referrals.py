def add_referral_bonus(inviter_profile, deal_commission):
    # 20% от комиссии сделки — на баланс USDT
    bonus = deal_commission * 0.2
    inviter_profile.balance_usdt += bonus
    inviter_profile.save()
